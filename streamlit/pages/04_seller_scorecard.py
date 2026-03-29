import streamlit as st
import pandas as pd
from src.db.db_connect import get_engine

st.set_page_config(page_title="Seller Scorecard", layout="wide")
st.title("Seller Scorecard")

engine = get_engine()
df = pd.read_sql("select * from mart_seller_scorecard order by revenue_rank", engine)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Top Sellers by Revenue")
    st.dataframe(df.nsmallest(20, "revenue_rank"), use_container_width=True)
with col2:
    st.subheader("Top Sellers by Rating")
    st.dataframe(df.nsmallest(20, "rating_rank"), use_container_width=True)
