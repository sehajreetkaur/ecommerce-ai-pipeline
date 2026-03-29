import os
import pandas as pd
from src.db.db_connect import get_engine

DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data/raw")

FILES = {
    "olist_orders": "olist_orders.csv",
    "olist_order_items": "olist_order_items.csv",
    "olist_products": "olist_products.csv",
    "olist_customers": "olist_customers.csv",
    "olist_sellers": "olist_sellers.csv",
    "olist_order_reviews": "olist_order_reviews.csv",
    "olist_order_payments": "olist_order_payments.csv",
}


def load_all():
    engine = get_engine()
    for table_name, filename in FILES.items():
        filepath = os.path.join(DATA_DIR, filename)
        df = pd.read_csv(filepath)
        df.to_sql(table_name, engine, if_exists="replace", index=False, schema="raw")
        print(f"Loaded {len(df)} rows into raw.{table_name}")


if __name__ == "__main__":
    load_all()
