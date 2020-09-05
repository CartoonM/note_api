from sqlalchemy import insert
from pymysql.err import IntegrityError

from .base_repository import BaseRepository
from .errors import EntityAlreadyExist
from database.models import Users
from schemas import UserInCreate
from services import security


class UserRepository(BaseRepository):

    async def create_user(self, user_create: UserInCreate):
        try:
            await self.database.execute(
                insert(Users).values(
                    username=user_create.username,
                    email=user_create.email,
                    password_hash=security.get_password_hash(
                                        user_create.password)))
        except IntegrityError:
            raise EntityAlreadyExist
