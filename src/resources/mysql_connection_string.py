from os import getenv

from dotenv import load_dotenv


def mysql_connection_string(enable_driver: bool = False) -> str:
    load_dotenv()
    return "mysql{}://{}:{}@{}:{}/{}".format(
        '+pymysql' if enable_driver else '',
        getenv("MYSQL_USER"),
        getenv("MYSQL_PASSWORD"),
        getenv("MYSQL_HOST"),
        getenv("MYSQL_PORT"),
        getenv("MYSQL_DATABASE")
    )
