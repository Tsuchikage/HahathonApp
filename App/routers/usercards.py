from App import models
from App.database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Path, APIRouter
from starlette import status
from .auth import get_current_user

router = APIRouter(prefix='/usercards',
                   tags=['usercards'])


def get_db():
    return SessionLocal()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users_cards(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(models.UsersCard).filter(models.UsersCard.owner_id == user.get('id')).all()


@router.get("/{user_card_id}", status_code=status.HTTP_200_OK)
async def get_user_card_by_id(user: user_dependency, db: db_dependency, user_card_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_card_model = db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).filter(
        models.UsersCard.owner_id == user.get('id')).first()
    if user_card_model is not None:
        return user_card_model
    raise HTTPException(status_code=404, detail='User card not found.')


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user_card(user: user_dependency, db: db_dependency, user_card_request: models.UsersCardRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_card_model = models.UsersCard(**user_card_request.dict(), owner_id=user.get('id'))
    db.add(user_card_model)
    db.commit()


@router.put("/update/{user_card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_card(user: user_dependency, db: db_dependency, user_card_request: models.UsersCardRequest,
                           user_card_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_card_model = db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).filter(
        models.UsersCard.owner_id == user.get('id')).first()
    if user_card_model is None:
        raise HTTPException(status_code=404, detail='User card not found.')
    user_card_model.user_card_name = user_card_request.user_card_name
    db.add(user_card_model)
    db.commit()


@router.delete("/delete/{user_card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_card(user: user_dependency, db: db_dependency, user_card_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_card_model = db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).filter(
        models.UsersCard.owner_id == user.get('id')).first()
    if user_card_model is None:
        raise HTTPException(status_code=404, detail='User card not found.')
    db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).filter(
        models.UsersCard.owner_id == user.get('id')).delete()
    db.commit()
