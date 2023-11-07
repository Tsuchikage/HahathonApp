from App import models
from App.database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Path, APIRouter
from starlette import status
from .auth import get_current_user

router = APIRouter(prefix='/admin',
                   tags=['admin'])


def get_db():
    return SessionLocal()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/usercards", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(models.UsersCard).all()


@router.delete("/usercards/{user_card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_usercard(user: user_dependency, db: db_dependency, user_card_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    usercard_model = db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).first()
    if usercard_model is None:
        raise HTTPException(status_code=404, detail='Usercard not found.')
    db.query(models.UsersCard).filter(models.UsersCard.id == user_card_id).delete()
    db.commit()
