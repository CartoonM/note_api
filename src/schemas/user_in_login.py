from pydantic import BaseModel


class UserInLogin(BaseModel):
    email: str
    password: str
