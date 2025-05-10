import uuid
from homeworks.baloghpeter.hw_09_fastapi.apiprogram import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy setup
DATABASE_URL = "sqlite:///./products.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# SQLAlchemy model
class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

# Pydantic models
class ProductCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ProductRead(ProductCreate):
    id: str

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint: List all products
@app.get("/products", response_model=List[ProductRead])
def list_products():
    db = next(get_db())
    return db.query(Product).all()

# Endpoint: Get a product by ID
@app.get("/products/{product_id}", response_model=ProductRead)
def get_product(product_id: str):
    db = next(get_db())
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Endpoint: Create a new product
@app.post("/products", response_model=ProductRead)
def create_product(product: ProductCreate):
    db = next(get_db())
    new_product = Product(
        id=str(uuid.uuid1()),
        item_name=product.item_name,
        quantity=product.quantity,
        price=product.price,
        category=product.category
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Endpoint: Update a product by ID
@app.put("/products/{product_id}", response_model=ProductRead)
def update_product(product_id: str, updated: ProductCreate):
    db = next(get_db())
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.item_name = updated.item_name
    product.quantity = updated.quantity
    product.price = updated.price
    product.category = updated.category
    db.commit()
    return product

# Endpoint: Delete a product by ID
@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    db = next(get_db())
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted successfully"}
