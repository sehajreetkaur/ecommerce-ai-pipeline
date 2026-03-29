import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from src.db.db_connect import get_engine


def load_product_features() -> pd.DataFrame:
    engine = get_engine()
    query = """
        select product_id, product_category_name, avg_price, total_orders
        from int_product_performance
    """
    return pd.read_sql(query, engine, index_col="product_id")


def compute_similarity_matrix(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include="number").columns
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[numeric_cols].fillna(0))
    sim = cosine_similarity(scaled)
    return pd.DataFrame(sim, index=df.index, columns=df.index)


def get_similar_products(product_id: str, top_n: int = 5) -> list:
    df = load_product_features()
    if product_id not in df.index:
        return []
    sim_matrix = compute_similarity_matrix(df)
    similar = sim_matrix[product_id].drop(product_id).nlargest(top_n)
    return similar.index.tolist()
