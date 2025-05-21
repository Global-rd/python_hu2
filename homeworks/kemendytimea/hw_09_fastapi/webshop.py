from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel, Field
import uuid

# Adatbázis beállítás
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# SQLAlchemy modell
class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid1()))
    item_name = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    category = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

# Pydantic modellek
class ProductBase(BaseModel):
    item_name: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., ge=0)
    category: str | None = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: str

    class Config:
        from_attributes = True

# FastAPI app és adatbázis session
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Végpontok
@app.get("/products/", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: str, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product.dict().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted"}

# Automatikus futtatás + böngésző megnyitása
if __name__ == "__main__":
    import uvicorn
    import webbrowser
    import threading
    import time

    def open_browser():
        time.sleep(1)  # Vár egy pillanatot, hogy a szerver elinduljon
        webbrowser.open("http://127.0.0.1:8000/docs")

    threading.Thread(target=open_browser).start()
    uvicorn.run("webshop:app", host="127.0.0.1", port=8000, reload=True)
