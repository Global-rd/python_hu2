"""
This module will handle the database connection for our webshop inventory application.
It sets up SQLAlchemy and creates the necessary database objects.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get the current directory where this file is located
# This will helps in creating the database file in the right place
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the database URL
# I am using SQLite because that's the only thing I know so far :D
database_path = os.path.join(current_dir, 'webshop.db')
SQLALCHEMY_DATABASE_URL = "sqlite:///" + database_path

# DB engine
# The check_same_thread = False option is needed for SQLite when used with FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal class - to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for inheritence
Base = declarative_base()

def get_db():
    """
    This function creates a new database session for each request
    and closes it when the request is done.
    
    Returns:
        SQLAlchemy session: A database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()