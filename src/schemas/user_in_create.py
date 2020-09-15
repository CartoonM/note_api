from pydantic import BaseModel, validator

from resources import constants
from helpers import check_email


class UserInCreate(BaseModel):
    username: str
    email: str
    password: str

    @validator('password')
    def password_length(cls, password):
        if (
            len(password) < constants.MAX_PASSWORD_LENGTH
            or
            len(password) > constants.MAX_PASSWORD_LENGTH
                ):
            raise ValueError("Password is too long or short")
        return password

    @validator('email')
    def validate_email(cls, email):
        return check_email(email)
