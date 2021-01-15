from datetime import datetime

from pydantic import BaseModel


class UserInDb(BaseModel):
    id: int
    username: str
    email: str
    password_hash: str
    created_at: datetime
