from databases import Database
from fastapi import FastAPI

from resources import mysql_connection_string_for_app


async def connect_to_db(app: FastAPI) -> None:
    database = Database(mysql_connection_string_for_app())
    await database.connect()
    app.state.db = database
