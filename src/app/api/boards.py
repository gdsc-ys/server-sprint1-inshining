import os

from fastapi import APIRouter
from db.sql import select_many_sql, select_one_sql, write_sql
from schemas.board import BoardCreate, BoardUpdate

router = APIRouter()

@router.get("/")
def get_boards():
    result = select_many_sql("SELECT * FROM board")
    return result

# 게시물 생성 api
@router.post("/new")
def create_board(board : BoardCreate):
    write_sql("INSERT INTO board(title, content) VALUES (%s, %s)", (board.title, board.content))
    return board

# 게시물 하나 조회
@router.get("/{board_id}")
def get_board(board_id):
    result = select_one_sql(f"SELECT * FROM board WHERE id = {board_id}")
    return result

# 게시물 하나 업데이트
@router.put("/board/{board_id}")
def update_board(board_id, board: BoardUpdate):
    write_sql(f"UPDATE board SET title = %s , content = %s WHERE id = %s", (board.title, board.content, board_id))
    return board


# 게시물 하나 삭제
@router.delete("/board/{board_id}")
def delete_board(board_id):
    write_sql("DELETE FROM board WHERE id = %s", (board_id))
    return {"msg" : "success"}

