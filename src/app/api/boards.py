import os

from fastapi import APIRouter
import psycopg2

from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

@router.get("/")
async def get_boards():
    with psycopg2.connect(f'postgres://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}?sslmode=require') as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM board')
            print(cur.fetchall())

    return "Hello"
