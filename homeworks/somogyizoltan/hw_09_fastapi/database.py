from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine 
from sqlalchemy.orm import sessionmaker, declarative_base 

# Ezt az órai anyagból hoztam egy kis átalakítással
DATABASE_URL = "sqlite+aiosqlite:///./webshop_items.db"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session