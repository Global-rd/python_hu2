from sqlalchemy import String, Integer, ForeignKey, Date, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid1
from datetime import date
from pydantic import BaseModel, Field
from typing import Optional, Annotated, List
from database import Base

#database model
class Product(Base):
    __tablename__ = "products"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

class ProductItem(Base):
    __tablename__ = "product_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), nullable=False)
    purchase_date: Mapped[date] = mapped_column(Date, nullable=False)
    expiry_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    invoice_number: Mapped[str] = mapped_column(String(100), nullable=False)    

#pydantic model
class ProductRequest(BaseModel):
    item_name: Annotated[str, Field(min_length=2, max_length=255)]
    price: Annotated[int, Field(gt=0)]
    category: Optional[Annotated[str, Field(max_length=100)]] = None

class ProductUpdateRequest(BaseModel):
    item_name: Optional[Annotated[str, Field(min_length=2, max_length=255)]] = None
    price: Optional[Annotated[int, Field(gt=0)]] = None
    category: Optional[Annotated[str, Field(max_length=100)]] = None    

class ProductResponse(ProductRequest):
    id: str
    stock_quantity: int

    model_config = {"from_attributes": True}

class ProductItemRequest(BaseModel):
    purchase_date: date
    expiry_date: Optional[date] = None
    invoice_number: str = Field(max_length=100)

class ProductItemUpdateRequest(BaseModel):
    purchase_date: Optional[date] = None
    expiry_date: Optional[date] = None
    invoice_number: Optional[Annotated[str, Field(max_length=100)]] = None

class ProductItemResponse(ProductItemRequest):
    id: int

    model_config = {"from_attributes": True}

class ProductWithItemsResponse(BaseModel):
    id: str
    item_name: str
    price: int
    category: Optional[str]
    stock_quantity: int
    items: List[ProductItemResponse] = []

    model_config = {"from_attributes": True}