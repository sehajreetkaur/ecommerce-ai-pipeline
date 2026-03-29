import streamlit as st
import pandas as pd
from src.db.db_connect import get_engine

st.set_page_config(page_title="Product Performance", layout="wide")
st.title("Product Performance")

engine = get_engine()
df = pd.read_sql("select * from mart_top_products order by revenue_rank", engine)

st.subheader("Top Products by Revenue")
st.dataframe(df.head(50), use_container_width=True)

st.subheader("Revenue by Category")
by_category = (
    df.groupby("product_category_name")["total_revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
)
st.bar_chart(by_category)
