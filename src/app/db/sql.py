import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

DB_INFO = f'postgres://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}?sslmode=require'

def write_sql(sql, value):
    with psycopg2.connect(DB_INFO) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, value)
        conn.commit()

def select_one_sql(sql):
    with psycopg2.connect(DB_INFO) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

def select_many_sql(sql):
    with psycopg2.connect(DB_INFO) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
