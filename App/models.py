from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String

from database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)


class ProductRequest(BaseModel):
    name: str = Field(min_length=3)
