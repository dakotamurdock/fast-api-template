from os import getenv
from dotenv import load_dotenv

load_dotenv()

APP_ENV = getenv('APP_ENV')
DATABASE_USERNAME = getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = getenv('DATABASE_PASSWORD')
DATABASE_HOST = getenv('DATABASE_HOST')
DATABASE_NAME = getenv('DATABASE_NAME')
TEST_DATABASE_NAME = getenv('DATABASE_NAME')
