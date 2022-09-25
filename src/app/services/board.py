from schemas.board import BoardCreate


class BoardService:
    def create_board(self, board: BoardCreate):
        board_db.save_board(board)
        return board

    def get_boards(self):
        result = board_db.retrieve_boards()
        return result

