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
    return {"status": "ok"}


@router.get("/list/")
async def get_notes(
    user: dict = Depends(get_current_user),
    note_repo: NoteRepository = Depends(get_repository(NoteRepository))
):
    return await note_repo.get_user_notes(user['id'])


@router.patch("/update/")
async def update_note(
    note: NoteInUpdate = Body(..., embed=True),
    user: dict = Depends(get_current_user),
    note_repo: NoteRepository = Depends(get_repository(NoteRepository))
):
    try:
        await note_repo.update_note(user['id'], note)
    except ParametersNotSpecified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Parameters for updating are not specified"
        )
    return {"status": "ok",
            "detail": "Note updated"}


@router.delete("/delete/")
async def delete_note(
    note: NoteInUpdate = Body(..., embed=True),
    user: dict = Depends(get_current_user),
    note_repo: NoteRepository = Depends(get_repository(NoteRepository))
):
    await note_repo.delete_note(user['id'], note)
    return {"status": "ok",
            "detail": "Note deleted"}
