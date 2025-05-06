from sqlalchemy import Column, String, Integer, Float
from database import Base
import uuid

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid1()))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=True)

    