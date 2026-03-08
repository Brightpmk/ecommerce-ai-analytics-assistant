from __future__ import annotations
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
import logging
import pandas as pd
from app.config import Config

_engine: Engine | None = None

def get_engine() -> Engine:
    global _engine
    if _engine is None:
        _engine = create_engine(Config.DATABASE_URL, pool_pre_ping=True)
    return _engine


def run_select_query(sql: str) -> pd.DataFrame:
    with get_engine().connect() as connection:
        return pd.read_sql(text(sql), connection)


def test_connection() -> bool:
    try:
        with get_engine().connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        logging.exception("Database connection failed.")
        return False
