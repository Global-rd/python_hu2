"""
This script tests the database connection for our webshop application.
It tries to connect to the database and execute a query.
"""

import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


def get_database_path():
    """
    Get the path to the database file.
    Ideally should return:
        str: The path to the database file
    """
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create the path to the database file
    db_path = os.path.join(current_dir, "webshop.db")
    
    print("Database path:", db_path)
    return db_path

def create_database_connection():
    """
    Create a connection to the database.
    
    Returns: engine and session_maker
    """
    # Get the path to the database
    db_path = get_database_path()
    
    # Create the database URL
    database_url = "sqlite:///" + db_path
    print("Database URL:", database_url)
    
    # Create the database engine
    print("Creating database engine...")
    engine = create_engine(
        database_url, connect_args={"check_same_thread": False}
    )
    
    # Create the session maker
    print("Creating session maker...")
    session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    return engine, session_maker

def test_database_connection():
    """
    Test if we can connect to the DB.

    Returns True if connection successful
    """
    print("\n--- Testing Database Connection ---")
    
    # Create database connection
    _, session_maker = create_database_connection()
    
    # Try to connect and execute a query
    print("Attempting to connect to database...")
    try:
        # Create a session
        db = session_maker()
        
        # Execute a simple query
        print("Executing test query...")
        db.execute(text("SELECT 1"))
        
        # Close the session
        print("Closing database session...")
        db.close()
        
        print("Database connection successful!")
        return True
    except Exception as e:
        print("Database connection failed!")
        print("Error:", str(e))
        return False
    
def check_database_file():
    """
    Check if the database file exists.
    
    Returns: True if file exists
    """
    print("\n--- Checking Database File ---")
    
    # Get the path to the database
    db_path = get_database_path()
    
    # Check if the file exists
    if os.path.exists(db_path):
        print("Database file exists at:", db_path)
        return True
    else:
        print("Database file does not exist!")
        return False
    
# Main execution
if __name__ == "__main__":
    print("Starting database connection test...")
    
    # Test the database connection
    connection_result = test_database_connection()
    
    # Check if the database file exists
    file_result = check_database_file()
    
    # Print final result
    print("\n--- Final Result ---")
    if connection_result and file_result:
        print("All tests passed! Database is ready to use. Yay!")
    else:
        print("Ajjajj! Some tests failed. Please check the errors above.")