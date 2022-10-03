from psycopg2._psycopg import cursor

from repository.user import UserRepository
from schemas.user import UserCreate, User

class UserService:
    def __init__(self):
        self.db = UserRepository()

    def create(self, cursor, user_obj : UserCreate ) -> User:
        user = self.db.save_user(cursor, user_obj)
        return user

    def get_user_by_username(self, cursor : cursor ,username : str):
        result = self.db.retrieve_user_by_username(cursor, username)
        return result

    def __del__(self):
        del self.db


user_service = UserService