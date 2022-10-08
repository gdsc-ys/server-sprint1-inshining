from config.security import verify_password
from db.sql import select_one_sql, select_many_sql
from schemas.user import UserCreate, User

class UserService:
    def create(self, cursor, user_obj : UserCreate ) -> User:
        user = self.db.save_user(cursor, user_obj)
        return user

    def authenticate(self, username: str, password: str):
        user = self.get_user_by_username(username)
        if not user:
            return None
        if not verify_password(password, user[2]):
            return None
        return user

    def get_user_by_username(self, username : str):
        user = select_many_sql(f"SELECT * FROM user WHERE username = {username}")
        return user


user_service = UserService()