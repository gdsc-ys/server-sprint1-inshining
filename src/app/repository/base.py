import os
from dotenv import load_dotenv

import psycopg2

from config.settings import get_session

load_dotenv()


class BaseRepository:
    def __init__(self, conn):
        self._conn = conn
        self._cur = self._conn.cursor()

    def __del__(self):
        self._cur.close()
        self._conn.close()
