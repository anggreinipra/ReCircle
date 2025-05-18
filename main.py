from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from app.database import db
from app.routes import register_blueprints
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Flask configuration
    if os.getenv("FLASK_ENV") == "development":
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")  # Use local database in development
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SUPABASE_DB_URL")  # Use Supabase database in production

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")  # JWT secret key from .env

    # Initialize extensions
    db.init_app(app)  # Initialize the database instance with Flask app
    jwt = JWTManager(app)  # Initialize JWT manager for handling authentication
    migrate = Migrate(app, db)  # Initialize Flask-Migrate for handling database migrations

    # Register blueprints for routes
    register_blueprints(app)  # Register all the routes for the app

    # Optional: Welcome route
    @app.route('/')
    def index():
        return {'message': 'Welcome to ReCircle API 🔐'}, 200

    return app

# Create the Flask application instance
app = create_app()

# Run the app only if the script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Running on all interfaces at port 5000
