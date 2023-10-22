from fastapi import FastAPI
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Path
from starlette import status
import models
from database import engine, SessionLocal
from routers import auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

def get_db():
    return SessionLocal()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/products", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(models.Product).all()


@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
async def read_product(db: db_dependency, product_id: int = Path(gt=0)):
    inventory_model = db.query(models.Product).filter(models.Product.id == product_id).first()
    if inventory_model is not None:
        return inventory_model
    raise HTTPException(status_code=404, detail='Product not found.')


@app.post("/create", status_code=status.HTTP_201_CREATED)
async def create_product(db: db_dependency, inventory_request: models.ProductRequest):
    inventory_model = models.Product(**inventory_request.dict())
    db.add(inventory_model)
    db.commit()


@app.put("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_product(db: db_dependency, product_request: models.ProductRequest, product_id: int = Path(gt=0)):
    inventory_model = db.query(models.Product).filter(models.Product.id == product_id).first()
    if inventory_model is None:
        raise HTTPException(status_code=404, detail='Product not found.')
    inventory_model.title = product_request.name
    inventory_model.price = product_request.price
    inventory_model.quantity = product_request.quantity
    db.add(inventory_model)
    db.commit()


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(db: db_dependency, inventory_id: int = Path(gt=0)):
    inventory_model = db.query(models.Product).filter(models.Product.id == inventory_id).first()
    if inventory_model is None:
        raise HTTPException(status_code=404, detail='Product not found.')
    db.query(models.Product).filter(models.Product.id == inventory_id).delete()
    db.commit()
