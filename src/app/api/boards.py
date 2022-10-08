import random

from fastapi import APIRouter

from db.redis import write_redis_obj, get_redis_obj
from db.sql import select_many_sql, select_one_sql, write_sql
from schemas.board import BoardCreate, BoardUpdate, Board
from faker import Faker

from services.board import board_service
import time

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
    start = time.process_time()
    result = board_service.retrieve_board(board_id)
    end = time.process_time()
    print("실행시간:", end-start)
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
    start_time = time.process_time()
    result = get_redis_obj(f"board_id:{board_id}")
    end_time = time.process_time()
    print("실행 시간 : ", end_time - start_time)
    return result

@router.get("/bulk-redis/{count}")
def get_boards_1000_by_redis(count: int):
    for i in range(count):
        start = time.process_time()
        for _ in range(1000):
            random_id = random.randint(1, 10000)
            board_service.retrieve_board(random_id)
        end = time.process_time()
        print(f"{i+1}회 실행 시간: ", end-start)
    return "completed"

@router.get("/bulk-db/{count}")
def get_boards_1000_by_db(count: int):
    for i in range(count):
        start = time.process_time()
        for _ in range(1000):
            random_id = random.randint(1, 10000)
            select_one_sql(
            f"SELECT board.id, board.title, board.content, (SELECT count(*) FROM comment WHERE board.id = comment.board_id) as comments FROM board WHERE board.id = {random_id}")
        end = time.process_time()
        print(f"{i+1}회 실행 시간: ", end-start)
    return "completed"