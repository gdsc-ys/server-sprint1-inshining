from db.redis import get_redis_obj, write_redis_obj
from db.sql import select_one_sql


class BoardService:
    def create_board(self):
        # self.db.save_board(board)
        # self.db.get_boards()
        pass

    def retrieve_board(self, board_id):
        redis_result = get_redis_obj(f"board_id:{board_id}")
        if redis_result is not None:
            return redis_result
        else:
            result = select_one_sql(f"SELECT board.id, board.title, board.content, (SELECT count(*) FROM comment WHERE board.id = comment.board_id) as comments FROM board WHERE board.id = {board_id}")
            (id, title, content, count_comment) = result
            board_dict = {"id": id, "title": title, "content": content, "count_comment": count_comment}
            write_redis_obj(f"board_id:{board_id}", board_dict)
        return result

board_service = BoardService()
