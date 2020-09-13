from sqlalchemy import insert, select, update, and_
from loguru import logger

from .base_repository import BaseRepository
from .errors import ParametersNotSpecified
from database.models import Notes
from schemas import NoteInCreate, NoteInUpdate


class NoteRepository(BaseRepository):

    async def create_note(
        self,
        note_create: NoteInCreate,
        user_id: int
    ) -> None:
        await self.database.execute(
            insert(Notes).values(
                title=note_create.title,
                body=note_create.body,
                user_id=user_id))

    async def get_user_notes(self, user_id: int):
        notes = await self.database.fetch_all(
            select([Notes]).where(Notes.user_id == user_id))
        return notes

    async def update_note(self, user_id: int, note: NoteInUpdate):
        try:
            assert note.body is not None or note.title is not None
        except AssertionError:
            logger.warning('Parameters for updating are not specified')
            raise ParametersNotSpecified
        note_update_values = note.dict()
        del note_update_values['id']
        keys = list(note_update_values.keys())
        for key in keys:
            if note_update_values[key] is None:
                del note_update_values[key]
        await self.database.execute(
            update(Notes).where(
                and_(Notes.id == note.id,
                     Notes.user_id == user_id)).values(
                         note_update_values))
