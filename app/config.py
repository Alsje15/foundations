from dotenv import load_dotenv
from os import environ

load_dotenv()

# Write condition to only use .replace with Heroku not locally
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
#.replace('postgresql://', 1)

SECRET_KEY = environ.get('SECRET_KEY')

RECIPES_PER_PAGE = 6
CHEFS_PER_PAGE = 6