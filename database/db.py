import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def connecttodb():
    conn = psycopg.connect(
        f"dbname='{os.getenv("DB_NAME")}' user='{os.getenv("POSTGRES_USER")}' host='{os.getenv('POSTGRES_HOST')}' password='{os.getenv("POSTGRES_PASSWORD")}' port='5432'"
    )
    return conn
