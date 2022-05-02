from dotenv import load_dotenv
from os import environ

load_dotenv()

# Only use .replace.. when running with Heroku not locally
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
#.replace('postgres://','postgresql://', 1)

SECRET_KEY = environ.get('SECRET_KEY')

RECIPES_PER_PAGE = 9
CHEFS_PER_PAGE = 9