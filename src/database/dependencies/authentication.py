from typing import Optional

from fastapi import Cookie, Depends, HTTPException, status

from .database import get_repository
from database.repositories import UserRepository
from database.repositories.errors import EntityDoesNotExist
from services import get_email_from_token


async def get_current_user(
    users_repo: UserRepository = Depends(get_repository(UserRepository)),
    token: Optional[str] = Cookie(None, alias='access_token')
) -> dict:
    try:
        email = get_email_from_token(token)
        user = await users_repo.get_user_by_email(email)
    except(ValueError, EntityDoesNotExist):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something happened to the token. Repeat authorization."
        )
    return user
