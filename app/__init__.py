# /app/__init__.py

import os
import logging

# Third-party imports
from flask import Flask, render_template

# Local imports
from app import database
from app.dash_setup import register_dashapps


def create_app():
    """Factory function that creates the Flask app"""

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    logging.basicConfig(level=logging.DEBUG)

    @app.route('/')
    def home():
        """Our only non-Dash route, to demonstrate that Flask can be used normally"""
        return render_template('index.html')

    # Initialize extensions
    database.init_app(app) # PostgreSQL db with psycopg2

    # For the Dash app
    register_dashapps(app)

    return app
