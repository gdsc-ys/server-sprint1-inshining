import os

from repository.base import BaseRepository
from dotenv import load_dotenv
from psycopg2._psycopg import cursor

load_dotenv()


class BoardRepository:
    def retrieve_boards(self, cursor: cursor):
        cursor.execute('SELECT * FROM board')
        return cursor.fetchall()

