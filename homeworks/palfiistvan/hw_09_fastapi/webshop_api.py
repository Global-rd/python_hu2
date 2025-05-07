from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import WsItem, WsItemRequest, WsItemResponse
from database import Base, engine, get_db
from typing import List

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 

app = FastAPI(lifespan=lifespan)

@app.get("/webshop/", response_model=List[WsItemResponse])
async def get_wsitem(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WsItem)) #SELECT * FROM Webshop
    Webshop = result.scalars().all()
    return Webshop

@app.post("/webshop/", response_model=WsItemResponse)
async def add_wsitem(wsitem:WsItemRequest, db: AsyncSession = Depends(get_db)):
    new_wsitem = WsItem(**wsitem.model_dump())

    db.add(new_wsitem)
    await db.commit()
    await db.refresh(new_wsitem)
    return new_wsitem

@app.get("/webshop/{wsitem_id}", response_model=WsItemResponse)
async def get_wsitem(wsitem_id: UUID, db: AsyncSession = Depends(get_db)):
    wsitem = await get_wsitem_by_id(wsitem_id, db)
    return wsitem 


@app.put("/webshop/{wsitem_id}", response_model=WsItemResponse)
async def update_wsitem(wsitem_id: UUID, wsitem_update: WsItemRequest, db: AsyncSession = Depends(get_db)):
    wsitem = await get_wsitem_by_id(wsitem_id, db)

    for key, value in wsitem_update.model_dump(exclude_unset=True).items():
        setattr(wsitem, key, value)

    db.add(wsitem)
    await db.commit()
    await db.refresh(wsitem)
    return wsitem


@app.delete("/webshop/{wsitem_id}", response_model=WsItemResponse)
async def delete_wsitem(wsitem_id: UUID, db: AsyncSession = Depends(get_db)):
    wsitem = await get_wsitem_by_id(wsitem_id, db)

    await db.delete(wsitem)
    await db.commit()
    return wsitem


async def get_wsitem_by_id(wsitem_id: UUID, db:AsyncSession):
    result = await db.execute(select(WsItem).where(WsItem.id == str(wsitem_id)))
    wsitem = result.scalar_one_or_none() 
    if not wsitem:
        raise HTTPException(status_code=404, detail=f"WsItem id {wsitem_id} not found")
    
    return wsitem