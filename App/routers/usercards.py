from App import models
from App.database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Path, APIRouter
from starlette import status

router = APIRouter(prefix='/usercards',
                   tags=['usercards'])


def get_db():
    return SessionLocal()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users_cards(db: db_dependency):
    return db.query(models.UsersCard).all()


@router.get("/{user_card_id}", status_code=status.HTTP_200_OK)
async def get_user_card_by_id(db: db_dependency, user_card_id: int = Path(gt=0)):
    user_card_model = db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).first()
    if user_card_model is not None:
        return user_card_model
    raise HTTPException(status_code=404, detail='User card not found.')


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user_card(db: db_dependency, user_card_request: models.UsersCardRequest):
    user_card_model = models.UsersCard(**user_card_request.dict())
    db.add(user_card_model)
    db.commit()


@router.put("/update/{user_card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_card(db: db_dependency, user_card_request: models.UsersCardRequest,
                           user_card_id: int = Path(gt=0)):
    user_card_model = db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).first()
    if user_card_model is None:
        raise HTTPException(status_code=404, detail='User card not found.')
    user_card_model.user_card_name = user_card_request.name
    db.add(user_card_model)
    db.commit()


@router.delete("/delete/{user_card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_card(db: db_dependency, user_card_id: int = Path(gt=0)):
    user_card_model = db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).first()
    if user_card_model is None:
        raise HTTPException(status_code=404, detail='User card not found.')
    db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).delete()
    db.commit()
