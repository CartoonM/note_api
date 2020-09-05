from sqlalchemy import insert, select

from .base_repository import BaseRepository
from database.models import Notes
from schemas import NoteInCreate


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
