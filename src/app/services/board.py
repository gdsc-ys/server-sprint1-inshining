from repository.board import BoardRepository
from schemas.board import BoardCreate
from psycopg2._psycopg import cursor


class BoardService:
    def __init__(self):
        self.db = BoardRepository()

    def create_board(self, board: BoardCreate):
        # self.db.save_board(board)
        # self.db.get_boards()

        return board

    def get_boards(self, cursor : cursor ):
        result = self.db.retrieve_boards(cursor)
        return result

board_service = BoardService()
