from fastapi import APIRouter, Body, Depends, HTTPException, Response, status

from services import ACCESS_TOKEN_EXPIRE_MINUTES
from schemas import UserInCreate, UserInLogin
from database.dependencies import get_repository
from database.repositories import UserRepository
from database.repositories.errors import (
    EntityAlreadyExist,
    EntityDoesNotExist,
    FailedCredentials
)


router = APIRouter()


@router.post("/auth/register/", status_code=status.HTTP_201_CREATED)
async def register(
    user_create: UserInCreate = Body(..., embed=True, alias="user"),
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
):
    try:
        await user_repo.create_user(user_create)
    except EntityAlreadyExist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )


@router.post("/auth/login/")
async def login(
    response: Response,
    user_login: UserInLogin = Body(..., embed=True, alias="user"),
    user_repo: UserRepository = Depends(get_repository(UserRepository))
):
    try:
        token = await user_repo.get_access_token(user_login)
    except(EntityDoesNotExist, FailedCredentials):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not exist or invalid credentials"
        )
    response.set_cookie(key="access_token",
                        value=token,
                        expires=ACCESS_TOKEN_EXPIRE_MINUTES * 60)
