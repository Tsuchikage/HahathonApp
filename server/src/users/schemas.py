from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, model_validator

from src.auth.utils import get_password_hash
from src.users.enums import Order, Roles, Sort
from src.core.schemas import PageSchema, PaginationSchema, ResponseSchema

from src.users.models import Status


class UserRequest(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None


class UserCreate(UserRequest):
    active: bool = True
    role: Roles = Roles.USER

    @model_validator(mode="after")
    def validator(cls, values: "UserCreate") -> "UserCreate":
        values.password = get_password_hash(values.password)
        return values


class UserResponse(ResponseSchema):
    username: str
    email: EmailStr
    first_name: str | None
    last_name: str | None
    country: str | None
    city: str | None
    telegram: str | None
    linkedin: str | None
    github: str | None
    status: Status | None
    industry: str | None
    experience_level: str | None
    language: str | None
    hard_skills: str | None
    soft_skills: str | None
    active: bool
    role: Roles
    create_date: datetime
    update_date: datetime


class UserUpdateRequest(BaseModel):
    username: str | None = None
    password: str | None = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    telegram: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    status: Optional[str] = None
    industry: Optional[str] = None
    experience_level: Optional[str] = None
    language: Optional[str] = None
    hard_skills: Optional[str] = None
    soft_skills: Optional[str] = None


class UserUpdateRequestAdmin(UserUpdateRequest):
    active: bool | None = None
    role: Roles | None = None


class UserUpdate(UserUpdateRequestAdmin):
    @model_validator(mode="after")
    def validator(cls, values: "UserUpdate") -> "UserUpdate":
        if password := values.password:
            values.password = get_password_hash(password)
        return values


class UserPage(PageSchema):
    users: list[UserResponse]


class UserPagination(PaginationSchema):
    sort: Sort = Sort.ID
    order: Order = Order.ASC


class UserId(BaseModel):
    user_id: int


class Username(BaseModel):
    username: str
