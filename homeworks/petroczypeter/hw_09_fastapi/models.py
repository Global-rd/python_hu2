"""
Now we define the data modells for our webshop inventory application.
It includes both SQLAlchemy models for the database and Pydantic models for the API.
"""
import uuid
from sqlalchemy import Column, String, Integer, Float
from pydantic import BaseModel
from typing import Optional

from database import Base

# SQLAlchemy model for database
class Product(Base):
    """
    Database model for a product in our inventory.
    
    Attributes:
        id: Unique identifier of the product
        item_name: e.g. morzsaporszívó
        quantity: Number of items in stock, e.g. 12
        price: Price of the product, e.g. 24900
        category: Optional field, the product's category
    """
    # Table name in the database
    __tablename__ = "products"
    
    # Define columns
    # We use uuid1 to generate a unique ID for each product
    id = Column(String, primary_key=True, index=True)
    item_name = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    category = Column(String, nullable=True)
    
    def __init__(self, **kwargs):
        """
        Initialize a new Product.
        If no ID is provided, generate a new UUID.
        """
        # If no ID is provided, generate one
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid.uuid1())
        super().__init__(**kwargs)

# Pydantic models for API
class ProductBase(BaseModel):
    """
    Base model with common product attributes.
    
    This defines the basic structure that all product-related models wil use.
    """
    item_name: str  # Name of the product (required)
    quantity: int   # Quantity in stock (required)
    price: float    # Price of the product (required)
    category: Optional[str] = None  # Category (optional)

# Model for creating a new product
class ProductCreate(ProductBase):
    """
    Model for creating a new product.
    
    This inherits all fields from ProductBase.
    We don't need to specify the ID as it will be generated automatically.
    """
    pass

# Model for updating an existing product
class ProductUpdate(BaseModel):
    """
    Model for updating an existing product.
    
    All fields are optional since we might want to update only some fields.
    """
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    category: Optional[str] = None

# Model for product responses from the API
class ProductResponse(ProductBase):
    """
    Model for product responses from the API.
    
    This includes all the base fields plusz the ID.
    """
    id: str  # Product ID (will be included in responses)
    
    class Config:
        """Configuration for the Pydantic model."""
        # This allows the model to read data from an ORM model (SQLAlchemy)
        from_attributes = True