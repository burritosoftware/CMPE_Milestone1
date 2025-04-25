from app import db
from flask_login import UserMixin
from datetime import datetime

# User class with one-to-many recipes relationship.
# The class inherits from UserMixin to implement critical flask-login functions automatically.

favorite_recipes = db.Table('favorite_recipes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32))
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    recipes = db.relationship("Recipe")
    comments = db.relationship('Comment', backref='author', lazy=True)
    # many to many for user - fav recipes
    favorite_recipes = db.relationship(
        'Recipe',
        secondary='favorite_recipes',
        backref='favorited_by'
    )


# Recipe class that links back to the author (user).
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    description = db.Column(db.String(32))
    ingredients = db.Column(db.String(32))
    instructions = db.Column(db.String(32))
    tags = db.Column(db.String(128))
    created = db.Column(db.DateTime(timezone=True))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='recipe', lazy=True, cascade="all, delete-orphan")

# Comment class that links back to the recipe
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1–5
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
