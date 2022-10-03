import os

from repository.base import BaseRepository
from dotenv import load_dotenv

load_dotenv()


class BoardRepository(BaseRepository):
    def retrieve_boards(self):
        self._cur.execute('SELECT * FROM board')
        return self._cur.fetchall()

