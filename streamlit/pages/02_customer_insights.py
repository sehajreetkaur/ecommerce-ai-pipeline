import streamlit as st
import pandas as pd
from src.db.db_connect import get_engine

st.set_page_config(page_title="Customer Insights", layout="wide")
st.title("Customer Insights")

engine = get_engine()
df = pd.read_sql("select * from mart_customer_summary", engine)

st.subheader("Customer Segments")
segment_counts = df["segment"].value_counts().reset_index()
segment_counts.columns = ["segment", "count"]
st.bar_chart(segment_counts.set_index("segment"))

st.subheader("Top Customers by Lifetime Value")
st.dataframe(
    df.sort_values("lifetime_value", ascending=False).head(20),
    use_container_width=True,
)
