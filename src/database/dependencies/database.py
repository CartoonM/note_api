from typing import Callable, Type

from databases import Database
from fastapi import Depends
from starlette.requests import Request

from database.repositories import BaseRepository


def _get_database(request: Request) -> Database:
    return request.app.state.db


def get_repository(
    repo_type: Type[BaseRepository],
) -> Callable[[Database], BaseRepository]:
    def _get_repo(
        db: Database = Depends(_get_database),
    ) -> Type[BaseRepository]:
        return repo_type(db)

    return _get_repo
