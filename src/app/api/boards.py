import os

from fastapi import APIRouter
from services.board import BoardService


router = APIRouter()

@router.get("/")
async def get_boards():
    service = BoardService()
    result = service.get_boards()

    return result
