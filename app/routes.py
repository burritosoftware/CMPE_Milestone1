from app import myapp_obj
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, SignupForm, RecipeForm, EditProfileForm
from app.models import User, Recipe, Comment
from app import db
from flask_login import login_required, login_user, logout_user, current_user
from datetime import datetime

### UNAUTHENTICATED ROUTES ###

# This route is the main page for the recipe app
@myapp_obj.route("/")
def main():
    return render_template("index.html")

# This route allows the user to view all the recipes
@myapp_obj.route("/recipes", methods=['GET', 'POST'])
def view_all_recipes():
    tag = request.args.get("tag", "").strip().lower()

    if tag:
        filtered = Recipe.query.filter(Recipe.tags.ilike(f"%{tag}%")).all()
    else:
        filtered = Recipe.query.all()

    recipes = [(r.title, User.query.get(r.author).username, r.id) for r in filtered]

    return render_template("all_recipes.html", recipes=recipes)

# This route allows the user to search for recipes using title or ingredient
# keywords
@myapp_obj.route('/search')
def search():
    query = request.args.get("query", "").lower().strip()
    keywords = query.split()

    # Filter recipes with keywords from title or ingredients
    recipes = Recipe.query.filter(
        db.or_(
            *[Recipe.title.ilike(f"%{keyword}%") for keyword in keywords] + 
            [Recipe.ingredients.ilike(f"%{keyword}%") for keyword in keywords]
        )
    ).all()
   
    # Check if recipes is empty or None
    if not recipes:
        print("No recipes found.")

    # Display search results
    return render_template("search_results.html", recipes=recipes, query=query)

@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user's password

        # Fetch a user by that username
        user = User.query.filter(User.username == form.username.data).first()
        if user:
            # Check that the passwords match
            if form.password.data == user.password:
                # Login the user, and remember the session if the box is checked
                login_user(user, remember=form.remember_me.data)

                next = request.args.get('next')

                return redirect(next or url_for('main'))
        
        # If the details were wrong, display an error and refresh to try again
        flash('Login details were incorrect.')
        return redirect(url_for('login'))
    
    # Display login form
    return render_template('login.html', form=form)

@myapp_obj.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # Check if this email or user exists already
        user1 = User.query.filter(User.username == form.username.data).first()
        user2 = User.query.filter(User.email == form.email.data).first()
        if user1 or user2:
            # If the user exists already, prevent signup.
            flash("This user already exists.")
            return redirect(url_for('signup'))
        
        # Create the new user, add them to the db, log them in
        new_user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        # Redirect to homepage
        return redirect(url_for('view_all_recipes'))
    
    # Display signup form
    return render_template('signup.html', form=form)



### AUTHENTICATED ROUTES ###
@myapp_obj.route("/logout")
@login_required
def logout():
    # Logout the user and bring them to the homepage
    logout_user()
    return redirect(url_for('view_all_recipes'))

@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        # Create a new recipe
        r = Recipe(title=form.title.data,
                   description=form.description.data,
                   ingredients=form.ingredients.data,
                   instructions=form.instructions.data,
                   tags=form.tags.data,
                   created=datetime.now(),
                   author=current_user.id) # Associate the recipe with the logged in user (one-to-many)
        # Save this recipe to the database
        db.session.add(r)
        db.session.commit()
        # Redirect to the recipe's details
        return redirect(f"/recipe/{r.id}")
    
    # Return recipe form page
    return render_template('create_recipe.html', form=form)

# This route allows user to view details of a single recipe
@myapp_obj.route("/recipe/<int:integer>")
@login_required
def view_single_recipe(integer):

    # Get the recipe ID from the route
    recipe = Recipe.query.get(integer)
    # Get the author from the recipe (used for showing author name)
    user = User.query.get(recipe.author)

    # Return recipe details page
    return render_template('view_recipe.html', recipe=recipe, user=user)


# This route deletes a recipe
@myapp_obj.route("/delete_recipe/<int:recipe_id>", methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    print("Deleting recipe") 
    # Get the recipe ID from the route
    recipe = Recipe.query.get(recipe_id)

    # Delete the recipe
    db.session.delete(recipe)
    db.session.commit()
    
    flash('Recipe deleted successfully.')
    #return redirect(url_for('index'))

    # Redirect back to view all recipes page
    return redirect(url_for('view_all_recipes'))

# This route adds a comment to a recipe
@myapp_obj.route('/add_comment/<int:recipe_id>', methods=['POST'])
def add_comment(recipe_id):
    
    # Get the form inputs for the content and ratings
    content = request.form['content']
    rating = int(request.form['rating'])
    
    # Get the logged-in user
    user = current_user 
    
    # Add comment to the database - many to one relationship with recipe
    new_comment = Comment(content=content, rating=rating, recipe_id=recipe_id, user_id=user.id)
    db.session.add(new_comment)
    db.session.commit()

    # Redirect back to same recipe page
    return redirect(url_for('view_single_recipe', integer=recipe_id))

# This route confirms a deletion of a recipe
@myapp_obj.route('/recipe/<int:recipe_id>/confirm_delete')
@login_required
def confirm_delete(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    return render_template('confirm_delete.html', recipe=recipe)

@myapp_obj.route('/myprofile', methods=['GET'])
@login_required
def view_user_profile():
    user = current_user
    user_data = User(
        id=user.id,
        email=user.email,
        username=user.username,
        recipes=user.recipes,
        comments=user.comments,
        favorite_recipes=user.favorite_recipes
    )
    return render_template('view_user_profile.html', user_data=user_data)

@myapp_obj.route('/edit_profile', methods=['POST'])
@login_required
def edit_user_profile():
    #why is this not being viewed
    form = EditProfileForm(obj=current_user) 

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.password = form.password.data
        current_user.email = form.email.data
        db.session.commit()
        flash("profile updated")
        return redirect(url_for('view_user_profile'))
    return render_template('edit_profile.html', form=form)

@myapp_obj.route('/toggle_favorite/<int:recipe_id>', methods=['POST'])
@login_required
def toggle_favorite(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe in current_user.favorite_recipes:
        current_user.favorite_recipes.remove(recipe)
    else:
        current_user.favorite_recipes.append(recipe)

    db.session.commit()
    return redirect(url_for('view_single_recipe', integer=recipe_id))



