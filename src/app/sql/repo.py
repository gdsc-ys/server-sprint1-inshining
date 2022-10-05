import os

import psycopg2


def get_cursor():
    try:
        conn = psycopg2.connect(
            f'postgres://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}?sslmode=require'
        )
        yield conn
    except Exception as e:
        print(e)
    finally:
        conn.close()

async def write_sql(sql, value):

    pass

async def select_one_sql(sql, value):
    pass

async def select_many_sql(sql, value):
    pass