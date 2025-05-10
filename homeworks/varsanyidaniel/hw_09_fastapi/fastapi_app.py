from models import Product, ProductRequest, ProductResponse
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from database import Base, engine, get_db
from sqlalchemy.future import select
from typing import List
from uuid import UUID

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 

app = FastAPI(lifespan=lifespan)



@app.get("/products/", response_model=List[ProductResponse])
async def get_all_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    return await get_product_by_id(product_id, db)

@app.post("/products/", response_model = ProductResponse)
async def add_product(product:ProductRequest, db: AsyncSession = Depends(get_db)):
    new_product=Product(**product.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: UUID, product_update: ProductRequest, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)
    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

@app.delete("/products/{product_id}", response_model=ProductResponse)
async def delete_movie(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)

    await db.delete(product)
    await db.commit()

    return product



async def get_product_by_id(product_id: UUID, db:AsyncSession):
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none() 
    if not product:
        raise HTTPException(status_code=404, detail=f"Error 404, Product ID {product_id} not found.")
    return product