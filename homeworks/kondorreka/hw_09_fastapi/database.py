#Aszinkron SQLAlchemy session és engine létrehozáshoz szükséges osztályok
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine 

#ORM (objektum-relációs leképezés) alaposztály és session kezelő
from sqlalchemy.orm import sessionmaker, declarative_base 

DATABASE_URL = "sqlite+aiosqlite:///./products.db" #SQLite adatbázis URL-je – aszinkron
engine = create_async_engine(DATABASE_URL, echo=True) #SQLAlchemy aszinkron használat #echo: SQL parancsok
#Aszinkron session factory: minden lekérdezéshez új session 
AsyncSessionLocal = sessionmaker(bind=engine, #adatbázis kapcsolat
                                class_=AsyncSession, #aszinkron session
                                expire_on_commit=False) #módosítások véglegesítése az adatbázisban, az objektum értékei elérhetők maradnak

#SQLAlchemy Base Class – ebből származtatjuk az adatbázistáblákat leíró osztályokat,
#így tudja a rendszer, hogy ezek az osztályok az adatbázissal vannak összekapcsolva
Base = declarative_base()

#Dependency- injection
#nem a függvény (vagy API-végpont) hozza létre a szükséges erőforrást, 
#hanem kívülről kapja meg automatikusan.
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session