# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Initialize the database object
db = SQLAlchemy()

def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__, template_folder='../templates')  # Point to the correct template folder
    

    # Load environment variables from .env file
    load_dotenv()

    # Configure the app with settings from config.py (Config class)
    app.config.from_object('config.Config')  # Ensure the 'config.Config' path is correct

    # Initialize the database with the app
    db.init_app(app)

    # Import routes and models inside the app context to avoid circular imports
    with app.app_context():
        from app import routes  # Import routes after the app is created
        from app.models import User, MenuItem, Order, Feedback  # Import models after app creation
        db.create_all()  # Create tables if they don't exist yet

    return app
