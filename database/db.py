"""
At the most fundamental level, SQLAlchemy's job is to relate Python classes to Database tables.
Python objects = rows in a database table.

The engine is set up to perform SQL operations on the database. The argument passed to create_engine
is the URL to the database. So, we are specifying the database to connect to. In this code below,
the exact database URL and credentials to access it are abstracted out so that the database can be
changed from the config file rather than in the code itself. This also makes the code reusable as a
starting point for other applications.

The declarative_base class creates a catalog of mapped Python classes -> database tables. When you
create a Python class in your application that should relate to a database table, you create a class
that inherits Base so that SQL Alchemy will handle the mapping of that new class and its objects
to the database table. In this application, this is done in the models.py file. If you head over
there, you will see class declarations that inherit base. These classes represent a table in the
database.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database import config

DATABASE_USERNAME = config.DATABASE_USERNAME
DATABASE_PASSWORD = config.DATABASE_PASSWORD
DATABASE_HOST = config.DATABASE_HOST
DATABASE_NAME = config.DATABASE_NAME

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
