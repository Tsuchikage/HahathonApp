from fastapi import FastAPI

from App import models
from App.database import engine
from App.routers import auth, usercards, admin, users

app = FastAPI(title='Hackathon App API')

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(usercards.router)
app.include_router(admin.router)
app.include_router(users.router)
