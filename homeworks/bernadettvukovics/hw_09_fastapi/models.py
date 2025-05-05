from uuid import UUID
from sqlalchemy import Column, String, Integer
from database import Base
from pydantic import BaseModel
from typing import Optional
from uuid import uuid1      #import uuid1
# SQLAlchemy model
class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=True)

# Pydantic schemas
class ProductCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ProductUpdate(BaseModel):
    item_name: Optional[str]
    quantity: Optional[int]
    price: Optional[int]
    category: Optional[str]

class ProductOut(ProductCreate):
    id: str