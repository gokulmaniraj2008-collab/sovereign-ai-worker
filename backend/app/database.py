from contextlib import contextmanager
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from psycopg import connect
from psycopg.rows import dict_row

from app.config import settings


def _database_url() -> str:
    """Normalize the runtime DB URL for managed PostgreSQL such as Supabase."""
    url = settings.database_url.strip()
    if not url:
        raise RuntimeError("DATABASE_URL is empty")

    # Supabase requires TLS. Do not overwrite an explicitly supplied SSL mode.
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    if parts.hostname and "supabase" in parts.hostname.lower():
        query.setdefault("sslmode", "require")
    query.setdefault("connect_timeout", "10")
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


@contextmanager
def get_conn():
    """Open a short-lived PostgreSQL connection using Render's DATABASE_URL."""
    with connect(_database_url(), row_factory=dict_row) as conn:
        yield conn
