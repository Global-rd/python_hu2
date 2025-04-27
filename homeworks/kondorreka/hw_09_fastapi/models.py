"""
Az adatbázis modell tartalmazza a következő oszlopokat (állíts be primary key-t is):
id (egyedi azonosító, pl uuid1 által generált)
item_name (pl: morzsaporszívó)
quantity (pl: 12)
price (pl: 24900)
category (ez a field legyen opcionális, pl: háztartási gép)"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from homeworks.kondorreka.hw_09_fastapi.database import Base

#database model
class Product(Base):
    __tablename__ = "products"
    product_id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[str] = Column(String, nullable=True)

#pydantic model
class ProductRequest(BaseModel):

    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ProductResponse(ProductRequest):
    product_id: UUID
    
