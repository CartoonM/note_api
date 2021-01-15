from pydantic import BaseModel


class NoteInCreate(BaseModel):
    title: str
    body: str
