from os import getenv

from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = getenv("SECRET_KEY", "test_secret_key")
JWT_SUBJECT = "access"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week
