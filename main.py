from fastapi import FastAPI
from fastapi.responses import JSONResponse

from server.core.database import engine
from server.users import models
from server.users.routers import router as guest_router, user_router
from server.auth.routers import router as auth_router
from server.core.security import JWTAuth
from starlette.middleware.authentication import AuthenticationMiddleware

app = FastAPI()
app.include_router(guest_router)
app.include_router(user_router)
app.include_router(auth_router)

# Add Middleware
app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())

models.Base.metadata.create_all(bind=engine)


@app.get('/')
def health_check():
    return JSONResponse(content={"status": "Running!"})
