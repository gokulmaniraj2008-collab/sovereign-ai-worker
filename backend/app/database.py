from contextlib import contextmanager
from psycopg import connect
from psycopg.rows import dict_row
from app.config import settings
@contextmanager
def get_conn():
    with connect(settings.database_url, row_factory=dict_row) as conn:
        yield conn
