from dotenv import load_dotenv
import os

load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = os.getenv("SUPABASE_DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SWAGGER = {
        'title': 'ReCircle Marketplace API',
        'uiversion': 3
    }
