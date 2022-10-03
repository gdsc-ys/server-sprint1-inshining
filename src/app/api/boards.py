import os

from fastapi import APIRouter, Depends

from config.settings import get_cursor
from services.board import board_service
from psycopg2._psycopg import cursor


router = APIRouter()

@router.get("/")
def get_boards(cursor : cursor = Depends(get_cursor)):
    result = board_service.get_boards(cursor)

    return result
