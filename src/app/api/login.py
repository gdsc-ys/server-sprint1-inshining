from fastapi import APIRouter, Depends

from config.settings import get_cursor
from services.board import board_service
from psycopg2._psycopg import cursor


router = APIRouter()

@router.post("/")
def login_user():
    pass