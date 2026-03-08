from __future__ import annotations
from pathlib import Path
import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from app.config import Config

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

FILE_TABLE_MAPPING = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_products_dataset.csv": "products",
    "product_category_name_translation.csv": "product_category_translation",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "order_payments",
}

def get_engine():
    return create_engine(Config.DATABASE_URL, pool_pre_ping=True)

def load_table(filename: str, table_name: str, engine) -> None:
    file_path = RAW_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    df = pd.read_csv(file_path)
    df = df.where(pd.notnull(df), None)

    print(f"Loading {filename} -> {table_name} ({len(df)} rows)")
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=1000,
    )
    print(f"Finished loading {table_name}")

def main() -> None:
    engine = get_engine()
    for filename, table_name in FILE_TABLE_MAPPING.items():
        load_table(filename, table_name, engine)

if __name__ == "__main__":
    main()