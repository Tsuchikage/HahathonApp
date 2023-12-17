from sqlalchemy import Boolean, Column, String, Enum as SQLAlchemyEnum
from enum import Enum
from src.core.models import Model

class Education(Enum):
    HIGH_SCHOOL = 'High school degree'
    ASSOCIATE = 'Associate degree'
    BACHELOR = 'Bachelor\'s degree'
    MASTER = 'Master\'s degree'
    DOCTORAL = 'Doctoral degree'


class User(Model):
    __tablename__ = "User"
    username = Column(name="username", type_=String, unique=True, index=True)
    password = Column(name="password", type_=String)
    email = Column(name="email", type_=String)
    country = Column(name="country", type_=String)
    city = Column(name="city", type_=String)
    telegram = Column(name="telegram", type_=String)
    linkedin = Column(name="linkedin", type_=String)
    github = Column(name="github", type_=String)
    education = Column(SQLAlchemyEnum(Education))
    industry = Column(name="industry", type_=String)
    experience_level = Column(name="experience_level", type_=String)
    language = Column(name="language", type_=String)
    hard_skills = Column(name="hard_skills", type_=String)
    soft_skills = Column(name="soft_skills", type_=String)
    first_name = Column(name="first_name", type_=String, nullable=True)
    last_name = Column(name="last_name", type_=String, nullable=True)
    active = Column(name="active", type_=Boolean)
    role = Column(name="role", type_=String)

