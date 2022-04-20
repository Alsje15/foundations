from dotenv import load_dotenv
from os import environ

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

RECIPES_PER_PAGE = 6
CHEFS_PER_PAGE = 6