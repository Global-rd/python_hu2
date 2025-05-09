from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import Items, ItemsRequest, ItemsResponse
from database import Base, engine, get_db
from typing import List

# Ez is az órai anyag megváltoztatva
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 

app = FastAPI(lifespan=lifespan)


@app.get("/webshop_items/", response_model=List[ItemsResponse])
async def get_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Items)) 
    items = result.scalars().all()
    
    return items

@app.post("/webshop_items/", response_model=ItemsResponse)
async def add_item(item:ItemsRequest, db: AsyncSession = Depends(get_db)):
    new_item = Items(**item.model_dump())

    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item

@app.get("/webshop_items/{item_id}", response_model=ItemsResponse)
async def get_items(item_id: UUID, db: AsyncSession = Depends(get_db)):
    item = await get_item_by_id(item_id, db)

    return item 

@app.put("/webshop_items/{item_id}", response_model=ItemsResponse)
async def update_item(item_id: UUID, item_update: ItemsRequest, db: AsyncSession = Depends(get_db)):
    item = await get_item_by_id(item_id, db)

    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(item, key, value)

    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@app.delete("/webshop_items/{item_id}", response_model=ItemsResponse)
async def delete_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    item = await get_item_by_id(item_id, db)

    await db.delete(item)
    await db.commit()

    return item



async def get_item_by_id(item_id: UUID, db:AsyncSession):
    result = await db.execute(select(Items).where(Items.id == str(item_id)))
    item = result.scalar_one_or_none() 
    if not item:
        raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")
    
    return item