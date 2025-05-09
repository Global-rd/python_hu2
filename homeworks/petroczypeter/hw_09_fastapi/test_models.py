"""
Let's test the Product model by creating a test product in the database
and then retrieving it to verify that it was saved corectly.
"""
import os
import random
from database import engine, Base, SessionLocal
from models import Product

def setup_database():
    """
    Set up the database by creating all tables.
    """
    print("Setting up database...")
    print("Creating tables if they don't exist...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully! Yay!")

def create_test_product():
    """
    Create a test product in the database.
    
    Returns:
        Product: The created product, or None if there was an error
    """
    print("\n--- Creating Test Product ---")
    
    # Generate random values for the product
    random_number = random.randint(1, 1000)
    random_quantity = random.randint(1, 100)
    random_price = round(random.uniform(10.0, 1000.0), 2)
    
    # Create a unique product name
    product_name = f"Test Product {random_number}"
    
    print(f"Generated random values:")
    print(f"  - Product name: {product_name}")
    print(f"  - Quantity: {random_quantity}")
    print(f"  - Price: {random_price}")
    
    # Create a database session
    print("Creating database session...")
    db = SessionLocal()

    try:
        # Create a test product
        print("Creating test product object...")
        test_product = Product(
            item_name=product_name,
            quantity=random_quantity,
            price=random_price,
            category="Test Category"
        )

        # Add to database and commit
        print("Adding product to database...")
        db.add(test_product)
        
        print("Committing changes...")
        db.commit()
        
        print("Refreshing product object...")
        db.refresh(test_product)
        
        print(f"Product created successfully with ID: {test_product.id}")
        return test_product
        
    except Exception as e:
        print("Error creating product:", str(e))
        print("Rolling back changes...")
        db.rollback()
        return None
    finally:
        print("Closing database session...")
        db.close()

def retrieve_product(product_id):
    """
    Retrieve a product from the database by ID.
    
    Args:
        product_id: The uuid of the product
        
    Returns: either the product or None if not found
    """
    print("\n--- Retrieving Product ---")
    
    # Create a database session
    print("Creating database session...")
    db = SessionLocal()
    
    try:
        # Query the product
        print(f"Querying product with ID: {product_id}")
        product = db.query(Product).filter(Product.id == product_id).first()
        
        if product:
            print("Product retrieved successfully! Yay!")
            print("Product details:")
            print(f"  - Name: {product.item_name}")
            print(f"  - Quantity: {product.quantity}")
            print(f"  - Price: {product.price}")
            print(f"  - Category: {product.category}")
            return product
        else:
            print("Product not found in database. Ajjajj!")
            return None
            
    except Exception as e:
        print(f"Error retrieving product: {str(e)}")
        return None
    finally:
        print("Closing database session...")
        db.close()

def check_database_file():
    """
    Check if the database file exists.
    """
    print("\n--- Checking Database File ---")
    
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create the path to the database file
    db_path = os.path.join(current_dir, "webshop.db")
    
    # Check if the file exists
    if os.path.exists(db_path):
        print(f"Database file exists at: {db_path}")
    else:
        print("Database file does not exist.")

def run_test():
    """
    Run the full test process.
    """
    print("Starting model test...")
    
    # Set up the database
    setup_database()
    
    # Create a test product
    test_product = create_test_product()
    
    # If product was created successfully, try to retrieve it
    if test_product:
        retrieved_product = retrieve_product(test_product.id)
        
        # Check if retrieval was successful
        if retrieved_product:
            print("\n--- Test Result ---")
            print("Test PASSED! Product was created and retrieved successfully. YAAAY!")
        else:
            print("\n--- Test Result ---")
            print("Test FAILED! Product was created but could not be retrieved. Ajjajj!")
    else:
        print("\n--- Test Result ---")
        print("Test FAILED! Could not create test product. Ajjajj!")
    
    # Check if the database file exists
    check_database_file()

# Make sure this is actually called
if __name__ == "__main__":
    print("Script started")
    run_test()
    print("Script finished")
