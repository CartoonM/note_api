from fastapi import APIRouter, Body, Depends, HTTPException, Response, status

from database.dependencies import get_current_user, get_repository
from database.repositories import NoteRepository
from database.repositories.errors import ParametersNotSpecified
from schemas import NoteInCreate, NoteInUpdate


router = APIRouter()


@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_note(
    note: NoteInCreate = Body(..., embed=True),
    user: dict = Depends(get_current_user),
    note_repo: NoteRepository = Depends(get_repository(NoteRepository))
):
    await note_repo.create_note(note, user['id'])


@router.get("/notes/list/")
async def get_notes(
    user: dict = Depends(get_current_user),
    note_repo: NoteRepository = Depends(get_repository(NoteRepository))
):
    return await note_repo.get_user_notes(user['id'])
