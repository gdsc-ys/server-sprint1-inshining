import os

from fastapi import APIRouter

from dotenv import load_dotenv

from services.board import BoardService

load_dotenv()

router = APIRouter()

@router.get("/")
async def get_boards():
    service = BoardService()
    result = service.get_boards()
    print(result)

    return result
