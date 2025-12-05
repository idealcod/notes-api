import time
import psycopg2
from psycopg2 import OperationalError

DB_HOST = "notes-db"
DB_NAME = "notes"
DB_USER = "user"
DB_PASSWORD = "pass"

def get_conn(retries=10, delay=2):
    """
    Подключение к PostgreSQL с повторными попытками, пока база не станет доступна
    """
    for i in range(retries):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            return conn
        except OperationalError:
            print(f"[{i+1}/{retries}] База недоступна, пробуем через {delay}s...")
            time.sleep(delay)
    raise Exception("Не удалось подключиться к базе данных")
