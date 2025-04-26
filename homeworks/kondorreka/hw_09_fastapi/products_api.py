"""
Hozz létre egy FastAPI app-ot ami egy képzeletbeli webshop termék
nyílvántartójaként működik az alapvető CRUD endpoint-okkal.
"""

from fastapi import FastAPI, HTTPException, Depends  # FastAPI app létrehozása, hibakezelés, és külső függőségek
from sqlalchemy.ext.asyncio import AsyncSession  # Aszinkron folyamatok
from sqlalchemy.future import select  # Adatbázis lekérdezések 
from uuid import UUID  # Egyedi azonosítók típuskezeléséhez
from contextlib import asynccontextmanager  # Aszinkron kontextuskezelő 
from homeworks.kondorreka.hw_09_fastapi.models import Product, ProductRequest, ProductResponse
from homeworks.kondorreka.hw_09_fastapi.database import Base, engine, get_db  
from typing import List  # Típusellenőrzéséhez

@asynccontextmanager #aszinkron kontextuskezelő dekorátor
async def lifespan(app: FastAPI): #életciklus függvény
    async with engine.begin() as conn: #adatbázis-kapcsolatot nyit írásra
        await conn.run_sync(Base.metadata.create_all) #tábla létrehozása, ha nincs
    yield #app indulási pont, ezután elkezdi kiszolgálni a kéréseket

app = FastAPI(lifespan=lifespan) #lifespan függvény hozzárendelése az app indulásához és leállásához.

"""
A típusokat válaszd meg a bennük tárolt adatoknak megfelelően. Az endpoint-ok
segítségével a következőkre kell alkalmasnak lennie az app-nak:

- Minden termék listázása"""
@app.get("/products/", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product)) #SELECT * FROM products
    products = result.scalars().all()
    
    return products

##- 1 termék hozzáadása (ne kelljen id-t megadni, de a response-ban legyen
#benne miután létrejött)
@app.post("/products/", response_model=ProductResponse)
async def add_product(product:ProductRequest, db: AsyncSession = Depends(get_db)):
    new_product = Product(**product.model_dump())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product

#- 1 termék listázása id alapján
@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)

    return product 

#- 1 termék adatainak frissítése id alapján
@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: UUID, product_update: ProductRequest, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)

    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

#- 1 termék törlése id alapján
@app.delete("/products/{product_id}", response_model=ProductResponse)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)

    await db.delete(product)
    await db.commit()

    return product


async def get_product_by_id(product_id: UUID, db:AsyncSession):
    result = await db.execute(select(Product).where(Product.product_id == str(product_id)))
    product = result.scalar_one_or_none() 
    if not product:
        raise HTTPException(status_code=404, detail=f"product id {product_id} not found")
    
    return product



#uvicorn homeworks.kondorreka.hw_09_fastapi.products_api:app --reload