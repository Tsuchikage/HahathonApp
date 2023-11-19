from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from App.database import Base


class UsersCard(Base):
    __tablename__ = 'usercards'

    id = Column(Integer, primary_key=True, index=True)
    user_card_name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    telegram_link = Column(String)


class UsersCardRequest(BaseModel):
    user_card_name: str = Field(min_length=3)
    telegram_link: str = Field(min_length=3)


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)


# class UsersRequest(BaseModel):
#     user_card_name: str = Field(min_length=3)
