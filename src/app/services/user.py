from config.settings import get_session


class UserService:
    def __init__(self):
        self.db = UserRepository(get_session())

    def create_user(self, ):
        self.db.save_board(board)
        self.db.get_boards()

        return board

    def get_user_by_username(self, username):
        result = self.db.retrieve_boards()
        return result

    def __del__(self):
        del self.db


user_service = UserService