from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import AsyncSessionLocal, engine, Base
from models import Product, ProductCreate, ProductUpdate, ProductOut
from typing import List
import uvicorn

app = FastAPI(title="Webshop Termék API")

# Dependency
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# Create DB table
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/products", response_model=List[ProductOut])
async def list_products(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product))
    return result.scalars().all()

@app.get("/products/{product_id}", response_model=ProductOut)
async def get_product(product_id: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=ProductOut)
async def create_product(product: ProductCreate, session: AsyncSession = Depends(get_session)):
    new_product = Product(**product.dict())
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    return new_product

@app.put("/products/{product_id}", response_model=ProductOut)
async def update_product(product_id: str, update: ProductUpdate, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product).where(Product.id == product_id))
    db_product = result.scalar_one_or_none()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in update.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    await session.commit()
    await session.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
async def delete_product(product_id: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product).where(Product.id == product_id))
    db_product = result.scalar_one_or_none()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    await session.delete(db_product)
    await session.commit()
    return {"detail": "Product deleted"}

# uvicorn prod_app:app --reload