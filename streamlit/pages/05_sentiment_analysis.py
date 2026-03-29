import streamlit as st
import pandas as pd
from src.db.db_connect import get_engine

st.set_page_config(page_title="Sentiment Analysis", layout="wide")
st.title("Review Sentiment Analysis")

engine = get_engine()
df = pd.read_sql("select * from int_review_sentiment", engine)

col1, col2, col3 = st.columns(3)
counts = df["sentiment_label"].value_counts()
col1.metric("Positive", counts.get("positive", 0))
col2.metric("Neutral", counts.get("neutral", 0))
col3.metric("Negative", counts.get("negative", 0))

st.subheader("Sentiment Distribution")
st.bar_chart(counts)

st.subheader("Recent Reviews")
st.dataframe(
    df.sort_values("review_creation_date", ascending=False).head(50),
    use_container_width=True,
)
