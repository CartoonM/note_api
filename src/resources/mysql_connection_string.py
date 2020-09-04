from os import getenv

from dotenv import load_dotenv


def mysql_connection_string_for_app() -> str:
    return "mysql://{}:{}@{}:{}/{}".format(
        getenv("MYSQL_USER"),
        getenv("MYSQL_PASSWORD"),
        getenv("MYSQL_HOST"),
        getenv("MYSQL_PORT"),
        getenv("MYSQL_DATABASE")
    )


def mysql_connection_string_for_alembic() -> str:
    return "mysql+pymysql://{}:{}@{}:{}/{}".format(
        getenv("MYSQL_USER"),
        getenv("MYSQL_PASSWORD"),
        getenv("MYSQL_HOST"),
        getenv("MYSQL_PORT"),
        getenv("MYSQL_DATABASE")
    )
