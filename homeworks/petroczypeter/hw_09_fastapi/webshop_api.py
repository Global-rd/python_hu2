"""
This is the main FastAPI application file for the webshop product inventory.
It defines all the API endpoints for managing products.
"""
import logging
import uuid
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from database import engine, Base, get_db
from models import Product, ProductCreate, ProductUpdate, ProductResponse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Create tables in the database if they don't exist
try:
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully!")
except Exception as e:
    logger.error(f"Error creating database tables: {str(e)}")

# Create FastAPI app
app = FastAPI(title="Webshop Product Inventory API")

# Helper functions
def find_product_by_id(product_id: str, db: Session) -> Product:
    """
    Find a product by its ID.
    
    Args:
        product_id: The ID of the product to find
        db: The database session
        
    Returns the product
        
    Raises:
        HTTPException: If the product is not found
    """
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            logger.warning(f"Product with ID {product_id} not found")
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except Exception as e:
        if isinstance(e, HTTPException):
            raise
        logger.error(f"Error finding product with ID {product_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Root endpoint
@app.get("/")
def read_root() -> Dict[str, str]:
    """
    Root endpoint that returns a welcome message.
    
    """
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Webshop Product Inventory API created by Peter!"}

# Get all products endpoint
@app.get("/products/", response_model=List[ProductResponse])
def get_all_products(db: Session = Depends(get_db)) -> List[Product]:
    """
    Get all products from the database.
    
    Args:
        db: The database session (injected by FastAPI)
        
    Returns A list of all products
    """
    try:
        logger.info("Getting all products from database...")
        products = db.query(Product).all()
        logger.info(f"Found {len(products)} products")
        return products
    except Exception as e:
        logger.error(f"Error retrieving products: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving products")

# Get a single product by ID endpoint
@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: str, db: Session = Depends(get_db)) -> Product:
    """
    Get a single product by its ID.
    
    Args:
        product_id: The ID of the product to get
        db: The database session (injected by FastAPI)
        
    Returns the requested product
        
    Raises:
        HTTPException: If the product is not found
    """
    logger.info(f"Getting product with ID: {product_id}")
    product = find_product_by_id(product_id, db)
    logger.info(f"Found product: {product.item_name}")
    return product

# Create a new product endpoint
@app.post("/products/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)) -> Product:
    """
    Create a new product.
    
    Args:
        product: The product data
        db: The database session (injected by FastAPI)
        
    Returns the created product
    """
    logger.info(f"Creating new product: {product.item_name}")
    
    
    try:
        # Generate a new UUID for the product
        new_id = str(uuid.uuid1())
        logger.info(f"Generated ID: {new_id}")
        
        # Create the product object
        db_product = Product(
            id=new_id,
            item_name=product.item_name,
            quantity=product.quantity,
            price=product.price,
            category=product.category
        )
        
        # Save to database
        logger.info("Saving product to database...")
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        
        logger.info(f"Product created successfully with ID: {db_product.id}. YAAAY!")
        return db_product
    except Exception as e:
        logger.error(f"Error creating product: {str(e)}")
        db.rollback()  # Roll back the transaction on error
        raise HTTPException(status_code=500, detail="Error creating product")

# Update a product endpoint
@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: str, product: ProductUpdate, db: Session = Depends(get_db)) -> Product:
    """
    Update an existing product.
    
    Args:
        product_id: The ID of the product to update
        product: The updated product data
        db: The database session (injected by FastAPI)
        
    Returns the updated product
        
    Raises:
        HTTPException: If the product is not found
    """
    logger.info(f"Updating product with ID: {product_id}")

    try:
        # Find the product
        db_product = find_product_by_id(product_id, db)
        
        # Update fields if provided
        logger.info("Updating product fields...")
        if product.item_name is not None:
            logger.info(f"Updating name to: {product.item_name}")
            db_product.item_name = product.item_name
            
        if product.quantity is not None:
            logger.info(f"Updating quantity to: {product.quantity}")
            db_product.quantity = product.quantity
            
        if product.price is not None:
            logger.info(f"Updating price to: {product.price}")
            db_product.price = product.price
            
        if product.category is not None:
            logger.info(f"Updating category to: {product.category}")
            db_product.category = product.category
        
        # Save changes
        logger.info("Saving changes to database...")
        db.commit()
        db.refresh(db_product)
        
        logger.info("Product updated successfully! AWESOME! :)")
        return db_product
    except Exception as e:
        if isinstance(e, HTTPException):
            raise
        logger.error(f"Error updating product with ID {product_id}: {str(e)}")
        db.rollback()  # Roll back the transaction on error
        raise HTTPException(status_code=500, detail="Error updating product")

# Delete a product
@app.delete("/products/{product_id}", status_code=status.HTTP_200_OK)
def delete_product(product_id: str, db: Session = Depends(get_db)) -> Dict[str, str]:
    """
    Delete a product.
    
    Args:
        product_id: The ID of the product to delete
        db: The database session (injected by FastAPI)
        
    Returns A success message
        
    Raises:
        HTTPException: If the product is not found
    """
    logger.info(f"Deleting product with ID: {product_id}")

    try:
        # Find the product
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product is None:
            logger.warning(f"Product with ID {product_id} not found for deletion")
            raise HTTPException(status_code=404, detail="Product not found")
        
        # Delete the product
        logger.info("Deleting product from database...")
        db.delete(db_product)
        db.commit()
        
        logger.info("Product deleted successfully")
        return {"message": "Product deleted successfully"}
    except Exception as e:
        if isinstance(e, HTTPException):
            raise
        logger.error(f"Error deleting product with ID {product_id}: {str(e)}")
        db.rollback()  # Roll back the transaction on error
        raise HTTPException(status_code=500, detail="Error deleting product")