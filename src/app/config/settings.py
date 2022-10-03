import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_session():
    try:
        conn = psycopg2.connect(
            f'postgres://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}?sslmode=require'
        )
    except Exception as e:
        print(e)
    else:
        return conn