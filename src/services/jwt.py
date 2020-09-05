from datetime import datetime, timedelta
from typing import Dict

import jwt
from pydantic import ValidationError

from resources import constants
from schemas import JWTMeta, JWTUser

JWT_SUBJECT = "access"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week


def create_jwt_token(
    *,
    jwt_content: Dict[str, str],
    secret_key: str,
    expires_delta: timedelta,
) -> str:
    to_encode = jwt_content.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update(JWTMeta(exp=expire, sub=JWT_SUBJECT).dict())
    return jwt.encode(to_encode, secret_key, algorithm=ALGORITHM).decode()


def create_access_token_for_user(user: dict) -> str:
    return create_jwt_token(
        jwt_content=JWTUser(email=user['email']).dict(),
        secret_key=constants.SECRET_KEY,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )


def get_email_from_token(token: str) -> str:
    try:
        return JWTUser(**jwt.decode(
            token,
            constants.SECRET_KEY,
            algorithms=[ALGORITHM])).email
    except jwt.PyJWTError as decode_error:
        raise ValueError("unable to decode JWT token") from decode_error
    except ValidationError as validation_error:
        raise ValueError("malformed payload in token") from validation_error
