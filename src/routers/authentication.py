from fastapi import APIRouter, Body, Depends, HTTPException, status

from schemas import UserInCreate
from database.repositories import UserRepository
from database.dependencies import get_repository
from database.repositories.errors import EntityAlreadyExist


router = APIRouter()


@router.post("/auth/register/", status_code=status.HTTP_201_CREATED)
async def register(
    user_create: UserInCreate = Body(..., embed=True),
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
):

    try:
        await user_repo.create_user(user_create)
    except EntityAlreadyExist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )
