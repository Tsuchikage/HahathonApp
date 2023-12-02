from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.auth import Admin, CurrentUser
from src.users.schemas import (
    UserPage,
    UserPagination,
    UserRequest,
    UserResponse,
    UserUpdateRequest,
)

from src.users.services import create_user, delete_user, list_users, update_user
from src.core.database import get_db
from src.core.schemas import ExceptionSchema

router = APIRouter(prefix="/user")


@router.post(
    "/",
    response_model=UserResponse,
    responses={
        status.HTTP_409_CONFLICT: {"model": ExceptionSchema},
    },
    status_code=status.HTTP_201_CREATED,
    tags=["user"],
)
async def user_create(
        user: UserRequest, db: AsyncSession = Depends(get_db)
) -> UserResponse:
    if created_user := await create_user(user=user, db=db):
        return created_user
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"User '{user.username}' already exists",
    )


@router.get(
    "/",
    response_model=UserResponse,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema}},
    tags=["user"],
)
async def user_get(user: CurrentUser) -> UserResponse:
    print("User in user_get:", user)
    return UserResponse.model_validate(user)


@router.put(
    "/",
    response_model=UserResponse,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema},
        status.HTTP_409_CONFLICT: {"model": ExceptionSchema},
    },
    tags=["user"],
)
async def user_update(
        user: CurrentUser,
        payload: UserUpdateRequest,
        db: AsyncSession = Depends(get_db),
) -> UserResponse:
    if updated_user := await update_user(user=user, payload=payload, db=db):
        return updated_user
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"User '{payload.username}' already exists",
    )


@router.delete(
    "/",
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema}},
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["user"],
)
async def user_delete(user: CurrentUser, db: AsyncSession = Depends(get_db)) -> None:
    await delete_user(user=user, db=db)
    return None


@router.get(
    "/admin",
    response_model=UserPage,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema}},
    tags=["admin"],
)
async def users_list(
        admin: Admin,
        pagination: UserPagination = Depends(),
        db: AsyncSession = Depends(get_db),
) -> UserPage:
    return await list_users(
        page=pagination.page,
        size=pagination.size,
        sort=pagination.sort,
        order=pagination.order,
        db=db,
    )

#
# @router.patch(
#     "/profile",
#     response_model=UserUpdateProfileResponse,
#     responses={
#         status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema},
#         status.HTTP_404_NOT_FOUND: {"model": ExceptionSchema},
#     },
#     tags=["user"],
# )
# async def user_update_profile(
#         user: CurrentUser,
#         payload: UserUpdateProfileRequest,
#         db: AsyncSession = Depends(get_db),
# ) -> UserUpdateProfileResponse:
#     if updated_profile := await update_user_profile(user=user, payload=payload, db=db):
#         return updated_profile
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"User profile not found",
#     )
#
#
# @router.get(
#     "/profile",
#     response_model=UserUpdateProfileResponse,
#     tags=["user"],
# )
# async def get_user_profile_endpoint(user: CurrentUser) -> UserUpdateProfileResponse:
#     return UserUpdateProfileResponse.model_validate(user)

