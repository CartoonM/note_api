from typing import Callable

from databases import Database
from fastapi import FastAPI

from resources import mysql_connection_string


def connect_to_db(app: FastAPI) -> Callable:

    async def start_app() -> None:
        database = Database(mysql_connection_string())
        app.state.db = database
        await database.connect()

    return start_app


def close_db_connection(app: FastAPI) -> Callable:

    async def stop_app() -> None:
        await app.state.db.disconnect()

    return stop_app
