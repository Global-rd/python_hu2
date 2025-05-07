from database import Base, engine, get_db
from models import Product, ProductRequest, ProductResponse
from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from uuid import UUID

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 

app = FastAPI(lifespan=lifespan)