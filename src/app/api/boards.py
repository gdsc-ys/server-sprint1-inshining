import os

from fastapi import APIRouter
from db.sql import select_many_sql, select_one_sql, write_sql
from schemas.board import BoardCreate, BoardUpdate
from schemas.comment import CommentCreate, CommentUpdate
from faker import Faker

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
    result = select_one_sql(f"SELECT board.id, board.title, board.content, (SELECT count(*) FROM comment WHERE board.id = comment.board_id) as comments FROM board WHERE board.id = {board_id}")
    return result

# 게시물 하나 업데이트
@router.put("/{board_id}")
def update_board(board_id, board: BoardUpdate):
    write_sql(f"UPDATE board SET title = %s , content = %s WHERE id = %s", (board.title, board.content, board_id))
    return board


# 게시물 하나 삭제
@router.delete("/{board_id}")
def delete_board(board_id):
    write_sql("DELETE FROM board WHERE id = %s", (board_id))
    return {"msg" : "success"}

@router.get("/comment/{comment_id}")
def get_comment(comment_id):
    result = select_one_sql(f"SELECT comment.id, comment.content, board.title, board.content  FROM comment LEFT OUTER JOIN board ON comment.board_id = board.id WHERE comment.id = {comment_id}")
    return result


@router.post("/{board_id}/comment")
def create_comment(board_id, comment: CommentCreate):
    write_sql("INSERT INTO comment(content, board_id) VALUES (%s, %s)", (comment.content, board_id))
    return comment

@router.put("/comment/{comment_id}")
def update_comment(comment_id, comment: CommentUpdate):
    write_sql(f"UPDATE comment SET content = %s WHERE id = %s", (comment.content, comment_id))
    return comment

@router.delete("/comment/{comment_id}")
def delete_comment(comment_id):
    write_sql("DELETE FROM comment WHERE id = %s", (comment_id))
    return {"msg": "success"}

@router.post("/bulk/{count_board}")
def create_boards(count_board : int):
    fake = Faker("ko_KR")
    titles = [fake.text(32) for _ in range(count_board)]
    contents = [fake.text(50) for _ in range(count_board)]
    write_sql("INSERT INTO board (title, content) SELECT UNNEST(%(unnest_title)s), UNNEST(%(unnest_content)s)", {"unnest_title": titles, "unnest_content": contents})
    return contents