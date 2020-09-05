from os import getenv

from dotenv import load_dotenv


load_dotenv()

SECRET_KEY: str = getenv("SECRET_KEY")
