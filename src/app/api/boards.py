import os

from fastapi import APIRouter, Depends

from config.settings import get_cursor
from services.board import board_service
from psycopg2._psycopg import cursor

from db.sql import select_many_sql

router = APIRouter()

@router.get("/")
def get_boards():
    result = select_many_sql("SELECT * FROM board")

    return result

# 게시물 생성 api
@router.post("/new")
def create_board():
    pass

# 게시물 하나 조회
@router.get("/board")
def get_board():
    pass

# 게시물 하나 업데이트
@router.put("/board/{board_id}")
def update_board():
    pass

# 게시물 하나 삭제
@router.delete("/board/{board_id}")
def delete_board():
    pass

