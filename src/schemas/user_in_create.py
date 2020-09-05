from pydantic import BaseModel


class UserInCreate(BaseModel):
    username: str
    email: str
    password: str
