from fastapi import FastAPI, HTTPException, Depends, Path, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, exists
from uuid import UUID
from contextlib import asynccontextmanager
from models import Product, ProductRequest, ProductResponse, ProductUpdateRequest, ProductItem, ProductItemRequest, ProductItemResponse, ProductWithItemsResponse, ProductItemUpdateRequest
from database import Base, engine, get_db
from typing import List

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 

app = FastAPI(lifespan=lifespan)

@app.get("/products/", response_model=List[ProductResponse])
async def list_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    products = result.scalars().all()

    count_result = await db.execute(
        select(ProductItem.product_id, func.count().label("stock_quantity"))
        .group_by(ProductItem.product_id)
    )
    item_counts = dict(count_result.all())

    response = [
        ProductResponse(
            id=product.id,
            item_name=product.item_name,
            price=product.price,
            category=product.category,
            stock_quantity=item_counts.get(product.id, 0)
        )
        for product in products
    ]
    
    return response

@app.post("/products/", response_model=ProductResponse, status_code=201)
async def add_product(product: ProductRequest, db: AsyncSession = Depends(get_db)):
    new_product = Product(**product.model_dump())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return ProductResponse(
        id=new_product.id,
        item_name=new_product.item_name,
        price=new_product.price,
        category=new_product.category,
        stock_quantity=0  # frissen létrehozott terméknél nincs készlet
    )

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    count_result = await db.execute(
        select(func.count()).where(ProductItem.product_id == product_id)
    )
    stock_quantity = count_result.scalar_one()
    
    return ProductResponse(
        id=product.id,
        item_name=product.item_name,
        price=product.price,
        category=product.category,
        stock_quantity=stock_quantity
    )

@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: str,
    updated_data: ProductUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if updated_data.item_name is not None and len(updated_data.item_name.strip()) < 2:      
        raise HTTPException(status_code=400, detail="item_name must be at least 2 characters long")

    if updated_data.price is not None and updated_data.price <= 0:
        raise HTTPException(status_code=400, detail="price must be a positive integer")

    if updated_data.item_name is not None:
        product.item_name = updated_data.item_name.strip()

    if updated_data.price is not None:
        product.price = updated_data.price

    if "category" in updated_data.__fields_set__:
        if updated_data.category == "":
            product.category = None
        else:
            product.category = updated_data.category

    await db.commit()
    await db.refresh(product)

    count_result = await db.execute(
        select(func.count()).where(ProductItem.product_id == product_id)
    )
    stock_quantity = count_result.scalar_one()

    return ProductResponse(
        id=product.id,
        item_name=product.item_name,
        price=product.price,
        category=product.category,
        stock_quantity=stock_quantity
    )

@app.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: str, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    item_exists_result = await db.execute(
        select(func.count()).where(ProductItem.product_id == product_id)
    )
    item_count = item_exists_result.scalar_one()

    if item_count > 0:
        raise HTTPException(status_code=400, detail="Product has items and cannot be deleted")

    await db.delete(product)
    await db.commit()

@app.post("/products/{product_id}/items", response_model=ProductItemResponse, status_code=201)
async def add_product_item(product_id: str, item: ProductItemRequest, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    new_item = ProductItem(
        product_id=product_id,
        purchase_date=item.purchase_date,
        expiry_date=item.expiry_date,
        invoice_number=item.invoice_number
    )

    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item

@app.get("/products/{product_id}/items/{id}", response_model=ProductItemResponse)
async def get_product_item(product_id: str, id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(ProductItem).where(
            ProductItem.id == id,
            ProductItem.product_id == product_id
        )
    )
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail="Product item not found")

    return item

@app.get("/products/{product_id}/items", response_model=ProductWithItemsResponse)
async def get_product_with_items(product_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    item_result = await db.execute(
        select(ProductItem).where(ProductItem.product_id == product_id)
    )
    items = item_result.scalars().all()

    stock_quantity = len(items)

    return ProductWithItemsResponse(
        id=product.id,
        item_name=product.item_name,
        price=product.price,
        category=product.category,
        stock_quantity=stock_quantity,
        items=items
    )

@app.delete("/products/{product_id}/items/{id}", status_code=204)
async def delete_product_item(product_id: str, id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(ProductItem).where(
            ProductItem.id == id,
            ProductItem.product_id == product_id
        )
    )
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail="Product item not found")

    await db.delete(item)
    await db.commit()

@app.put("/products/{product_id}/items/{id}", response_model=ProductItemResponse)
async def update_product_item(product_id: str, id: int, update_data: ProductItemUpdateRequest, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(ProductItem).where(
            ProductItem.id == id,
            ProductItem.product_id == product_id
        )
    )
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail="Product item not found")


    if update_data.purchase_date is not None:
        item.purchase_date = update_data.purchase_date

    if update_data.expiry_date is not None:
        item.expiry_date = update_data.expiry_date

    if "invoice_number" in update_data.__fields_set__:
        item.invoice_number = update_data.invoice_number

    await db.commit()
    await db.refresh(item)

    return item    