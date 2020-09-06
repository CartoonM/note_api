from loguru import logger
from sqlalchemy import insert, select
from pymysql.err import IntegrityError

from .base_repository import BaseRepository
from .errors import EntityAlreadyExist, EntityDoesNotExist, FailedCredentials
from database.models import Users
from schemas import UserInCreate, UserInLogin
from services import security, create_access_token_for_user


class UserRepository(BaseRepository):

    async def create_user(self, user_create: UserInCreate) -> None:
        try:
            password_hash = await security.get_password_hash(
                                            user_create.password)
            await self.database.execute(
                insert(Users).values(
                    username=user_create.username,
                    email=user_create.email,
                    password_hash=password_hash))
        except IntegrityError:
            logger.warning('User already exist')
            raise EntityAlreadyExist

    async def get_and_check_user(self, user_login: UserInLogin) -> dict:
        user = await self.database.fetch_one(
                    select([Users]).where(Users.email == user_login.email))
        if user is None:
            logger.warning('User does not exist')
            raise EntityDoesNotExist
        if not await security.verify_password(
            user_login.password,
            user['password_hash']
                ):
            logger.warning('Invalid password')
            raise FailedCredentials
        return dict(user)

    async def get_access_token(self, user_login: UserInLogin):
        user = await self.get_and_check_user(user_login)
        return create_access_token_for_user(user)

    async def get_user_by_email(self, email: str) -> dict:
        user = await self.database.fetch_one(
                    select([Users]).where(Users.email == email))
        if user is None:
            logger.warning('User does not exist')
            raise EntityDoesNotExist
        return dict(user)
