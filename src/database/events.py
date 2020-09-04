from databases import Database
from fastapi import FastAPI

from resources import mysql_connection_string


async def connect_to_db(app: FastAPI) -> None:
    database = Database(mysql_connection_string())
    await database.connect()
    app.state.db = database


async def close_db_connection(app: FastAPI) -> None:
    await app.state.db.disconnect()
