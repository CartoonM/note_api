from pydantic import BaseModel


class NoteInUpdate(BaseModel):
    id: int
    title: str = None
    body: str = None
