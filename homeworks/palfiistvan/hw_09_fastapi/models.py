from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from database import Base

#database model
class WsItem(Base):
    __tablename__ = "Webshop"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[Optional[str]] = Column(String, nullable=True)

#pydantic model
class WsItemRequest(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str]

class WsItemResponse(WsItemRequest):
    id: str
