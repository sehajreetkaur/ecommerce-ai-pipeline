import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.db.db_connect import get_engine


def build_user_item_matrix() -> pd.DataFrame:
    engine = get_engine()
    query = """
        select co.customer_unique_id, i.product_id, count(*) as purchase_count
        from int_customer_orders co
        join stg_order_items i using (order_id)
        group by co.customer_unique_id, i.product_id
    """
    df = pd.read_sql(query, engine)
    return df.pivot_table(
        index="customer_unique_id",
        columns="product_id",
        values="purchase_count",
        fill_value=0,
    )


def get_similar_customers(customer_id: str, matrix: pd.DataFrame, top_n: int = 10) -> list:
    if customer_id not in matrix.index:
        return []
    sim = cosine_similarity(matrix)
    sim_df = pd.DataFrame(sim, index=matrix.index, columns=matrix.index)
    similar = sim_df[customer_id].drop(customer_id).nlargest(top_n)
    return similar.index.tolist()


def recommend_products(customer_id: str, top_n: int = 5) -> list:
    matrix = build_user_item_matrix()
    similar_customers = get_similar_customers(customer_id, matrix)
    if not similar_customers:
        return []

    purchased = set(matrix.loc[customer_id][matrix.loc[customer_id] > 0].index)
    candidates = matrix.loc[similar_customers].sum().drop(index=list(purchased))
    return candidates.nlargest(top_n).index.tolist()
