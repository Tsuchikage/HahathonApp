from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas import Credentials, Refresh, Token
from src.auth.services import (
    authenticate_refresh_token,
    authenticate_user,
    generate_token,
)
from src.core.database import get_db
from src.core.schemas import ExceptionSchema

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/token",
    response_model=Token,
    responses={401: {"model": ExceptionSchema}},
)
async def token(credentials: Credentials, db: AsyncSession = Depends(get_db)) -> dict:
    if user := await authenticate_user(
            username=credentials.username,
            password=credentials.password,
            db=db,
    ):
        return await generate_token(
            user_id=user.id
        )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.post(
    "/refresh",
    response_model=Token,
    responses={401: {"model": ExceptionSchema}},
)
async def refresh(request: Refresh, db: AsyncSession = Depends(get_db)) -> dict:
    if new_token := await authenticate_refresh_token(
            token=request.refresh_token, db=db
    ):
        return new_token
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )
