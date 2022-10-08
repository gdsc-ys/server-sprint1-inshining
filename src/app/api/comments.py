from fastapi import APIRouter

from db.sql import select_one_sql, write_sql
from schemas.comment import CommentCreate, CommentUpdate

router = APIRouter()

@router.get("/{comment_id}")
def get_comment(comment_id):
    result = select_one_sql(f"SELECT comment.id, comment.content, board.title, board.content  FROM comment LEFT OUTER JOIN board ON comment.board_id = board.id WHERE comment.id = {comment_id}")
    return result


@router.post("/{board_id}")
def create_comment(board_id, comment: CommentCreate):
    write_sql("INSERT INTO comment(content, board_id) VALUES (%s, %s)", (comment.content, board_id))
    return comment

@router.put("/{comment_id}")
def update_comment(comment_id, comment: CommentUpdate):
    write_sql(f"UPDATE comment SET content = %s WHERE id = %s", (comment.content, comment_id))
    return comment

@router.delete("/{comment_id}")
def delete_comment(comment_id):
    write_sql("DELETE FROM comment WHERE id = %s", (comment_id))
    return {"msg": "success"}
