from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from typing import List
from models import WsItem, WsItemRequest, WsItemResponse
from database import Base, engine, get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/webshop/", response_model=List[WsItemResponse])
async def list_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WsItem))
    items = result.scalars().all()
    return items


@app.post("/webshop/", response_model=WsItemResponse)
async def create_item(item: WsItemRequest, db: AsyncSession = Depends(get_db)):
    new_item = WsItem(**item.model_dump())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item


@app.get("/webshop/{item_id}", response_model=WsItemResponse)
async def get_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    item = await fetch_item_by_id(item_id, db)
    return item


@app.put("/webshop/{item_id}", response_model=WsItemResponse)
async def update_item(item_id: UUID, item_update: WsItemRequest, db: AsyncSession = Depends(get_db)):
    item = await fetch_item_by_id(item_id, db)

    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(item, key, value)

    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@app.delete("/webshop/{item_id}", response_model=WsItemResponse)
async def delete_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    item = await fetch_item_by_id(item_id, db)
    await db.delete(item)
    await db.commit()
    return item


async def fetch_item_by_id(item_id: UUID, db: AsyncSession):
    result = await db.execute(select(WsItem).where(WsItem.id == str(item_id)))  # <- Itt a javítás
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found.")
    return item
