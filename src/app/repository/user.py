from config.security import convert_password_hash
from schemas.user import User, UserCreate

from psycopg2._psycopg import cursor, connection

class UserRepository:
    def save_user(self, cursor : cursor, user : UserCreate) -> User:
        hash_password = convert_password_hash(user.password)
        query = f"INSERT INTO user (username, password) VALUES (f{user.username}, f{hash_password})"
        cursor.execute(query)



    def get_user_by_username(self, cursor : cursor, username : str) -> User:
        cursor.execute('SELECT * FROM user')
        return cursor.fetchone()