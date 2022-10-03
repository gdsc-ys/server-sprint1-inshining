from config.settings import get_session
from repository.board import BoardRepository
from schemas.board import BoardCreate


class BoardService:
    def __init__(self):
        self.db = BoardRepository(get_session())

    def create_board(self, board: BoardCreate):
        self.db.save_board(board)
        self.db.get_boards()

        return board

    def get_boards(self):
        result = self.db.retrieve_boards()
        return result

    def __del__(self):
        del self.db

