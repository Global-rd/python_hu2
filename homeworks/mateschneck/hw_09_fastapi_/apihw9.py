from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import Optional, List
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# SQLite DB setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./products.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# SQLAlchemy model
class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, index=True)
    item_name = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Integer)
    category = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

# Pydantic schema
class ProductCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ProductOut(ProductCreate):
    id: str

# CRUD endpoints

@app.post("/products/", response_model=ProductOut)
def create_product(product: ProductCreate):
    db = SessionLocal()
    db_product = Product(
        id=str(uuid4()),
        item_name=product.item_name,
        quantity=product.quantity,
        price=product.price,
        category=product.category
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/", response_model=List[ProductOut])
def list_products():
    db = SessionLocal()
    return db.query(Product).all()

@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: str):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: str, updated: ProductCreate):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for attr, value in updated.dict().items():
        setattr(product, attr, value)
    db.commit()
    db.refresh(product)
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted"}