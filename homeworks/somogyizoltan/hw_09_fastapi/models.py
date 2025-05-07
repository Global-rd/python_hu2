from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from database import Base

# Ez is az órai anyagból van átmentve és átalakítva a megadás alapján

#database model
class Items(Base):
    __tablename__ = "webshop_items"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[str] = Column(String)
     

#pydantic model
class ItemsRequest(BaseModel):

    item_name: str
    quantity: int
    price: int
    category: Optional[str] = ""

class ItemsResponse(ItemsRequest):
    id: UUID


