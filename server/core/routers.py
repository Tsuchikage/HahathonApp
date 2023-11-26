from fastapi import APIRouter

from server.auth.routers import auth_router
from server.users.routers import users_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(users_router)
