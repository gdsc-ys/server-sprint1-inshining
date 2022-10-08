import json

import redis
from fastapi import APIRouter

from db.redis import write_redis_obj, get_redis_obj
from db.sql import select_many_sql, select_one_sql, write_sql
from schemas.board import BoardCreate, BoardUpdate, Board
from faker import Faker
from redis.commands.json.path import Path

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
    redis_result = get_redis_obj(f"board_id:{board_id}")
    if redis_result is not None:
        return redis_result
    else:
        result = select_one_sql(f"SELECT board.id, board.title, board.content, (SELECT count(*) FROM comment WHERE board.id = comment.board_id) as comments FROM board WHERE board.id = {board_id}")
        (id, title, content, count_comment) = result
        board_dict = {"id": id, "title": title, "content": content, "count_comment": count_comment}
        write_redis_obj(f"board_id:{board_id}", board_dict)
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

# bulk_board
@router.post("/bulk/{count_board}")
def create_boards(count_board : int):
    fake = Faker("ko_KR")
    titles = [fake.text(32) for _ in range(count_board)]
    contents = [fake.text(50) for _ in range(count_board)]
    write_sql("INSERT INTO board (title, content) SELECT UNNEST(%(unnest_title)s), UNNEST(%(unnest_content)s)", {"unnest_title": titles, "unnest_content": contents})
    return contents

@router.post("/redis-test/{board_id}")
def create_board_redis(board_id: int):
    (id, title, content, count_comment) = select_one_sql(f"SELECT board.id, board.title, board.content, (SELECT count(*) FROM comment WHERE board.id = comment.board_id) as comments FROM board WHERE board.id = {board_id}")
    board_dict = {"id": id, "title": title, "content": content, "count_comment": count_comment}
    write_redis_obj(f"board_id:{board_id}", board_dict)
    return (id, title, content, count_comment)

@router.get("/redis-test/{board_id}")
def get_board_by_redis(board_id):
    result = get_redis_obj(f"board_id:{board_id}")
    return result
