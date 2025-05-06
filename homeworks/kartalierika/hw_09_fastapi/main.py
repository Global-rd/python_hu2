from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from models import Product
from database import SessionLocal, engine, Base

#Adatbázis inicializálása
Base.metadata.create_all(bind=engine)
app = FastAPI()

#Dependency 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Pydantic sémák
class ProductCreate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None

class ProductOut(ProductCreate):
    id: str

#Endpointok
@app.post("/products", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products", response_model=List[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Item not found")
    return product

@app.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: str, updated: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in updated.dict().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(product)
    db.commit()
    return {"message": "Item deleted"}

