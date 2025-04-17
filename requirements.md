## Functional Requirements
1. A visitor can create an account by providing a username, email, and password.  
2. Registered users can log in using their email and password.  
3. Logged-in users can log out of their account securely.  
4. Logged-in users can add new recipes with title, description, ingredients, and instructions.  
5. Users can update their own recipes after creation.  
6. Users can delete their own recipes.  
7. Anyone can view the details of a recipe including ingredients and instructions.  
8. Users can search recipes by title or ingredient keywords.  
9. Users can rate a recipe from 1 to 5 stars.  
10. Users can leave comments on a recipe.  
11. Users can view their own profile, including their submitted recipes.  
12. Users can update their display name, email, or password.  
13. Users can save or 'favorite' recipes for quick access later.  
14. Homepage or main recipe list shows all recipes available in the database.  
15. Users can filter recipes by tags like 'vegan', 'dessert', etc.

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. non-functional
2. non-functional

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
1. User Registration
    - user must be on the index page
    - visitor clicks on login/register button
    - visitor inputs valid user,email,pass, into registration form,
    visitor submits registration form,
    system validates the provided information,
    system creates the account,
    system redirects visitor to login page
2. User Login
    - user must be on the login/register page
    - user must click on login button
    - user inputs valid user, pass, submits login,
    system validates login information,
    system redirects user to dashboard. 
3. User Logout
    - user must be logged in
    - user must click on logout butto
    - system recieves logout request,
    system clear session,
    user is redirected to login page
4. Create Recipe
    - user must be logged in and on index page
    - user clicks on create recipe button
    - user is redirected to new recipe form,
    user fills out new recipe form,
    system validates the provided recipe,
    system saves and links created recipe to user in db,
    user is returned to index,
5. Edit Recipe
    - user must be logged in and the creator of the recipe
    - user must click on edit recipe
    - user is redirected to edit recipe page,
    user inputs changes to recipe,
    user clicks done,
    system validates recipe,
    user is returned to view recipe
6. Delete Recipe
    - user must be logged in and the creator of the recipe
    - user must click on edit recipe, then click delete
    - user is asked to confirm deletion,
    system validates response,
    system queries db and deletes recipe,
    user is redirected to view index
7. View Recipe
    - visitor must be on index page, click view all button
    - visitor finds recipe of interest, clicks view recipe button
    - visitor is redirected to view recipe of given recipe..
8. Search Recipe
    - visitor is on index page
    - visitor clicks on search bar
    - visitor types in name, system fuzzy searches name,
    most matching is displayed sorted
9. Rate Recipe
    - user is logged in and viewing recipe
    - user clicks rate recipe button
    - a rating display is rendered for user,
    user selects number rating,
    user is prompted with optional text rating,
    user clicks submit,
    system validates response,
    user is redirected to view recipe
10. Comment on Recipe
    - user is logged in and viewing recipe
    - user clicks comment button
    - text box rendered for user,
    user enters text,
    user clicks submit,
    system validates entry, 
    system stores entry in db
11. View User Profile
    - user is logged in
    - user clicks my profile button in the top left
    - system redirects user to view user profile,
    user profile is rendered for user
12. 

10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>

1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...

