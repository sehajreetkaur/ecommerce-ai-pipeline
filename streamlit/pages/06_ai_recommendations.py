import streamlit as st
import pandas as pd
from src.db.db_connect import get_engine
from src.genai.recommend import get_recommendations
from src.genai.explain import generate_explanation
from components.recommendation_card import render_recommendation_card

st.set_page_config(page_title="AI Recommendations", layout="wide")
st.title("AI-Powered Product Recommendations")

engine = get_engine()
customers = pd.read_sql(
    "select customer_unique_id, segment, order_count, lifetime_value from mart_customer_summary limit 100",
    engine,
)

customer_id = st.selectbox("Select a customer", customers["customer_unique_id"].tolist())

if customer_id:
    profile = customers[customers["customer_unique_id"] == customer_id].iloc[0].to_dict()
    products = pd.read_sql(
        "select product_id, product_category_name, avg_price from mart_top_products limit 50",
        engine,
    ).to_dict(orient="records")

    if st.button("Generate Recommendations"):
        with st.spinner("Generating recommendations with Claude..."):
            recs = get_recommendations(profile, products)
            explanation = generate_explanation(
                profile["segment"],
                [r["product_name"] for r in recs],
                f"{profile['order_count']} orders, ${profile['lifetime_value']:.2f} LTV",
            )

        st.info(explanation)
        for rec in recs:
            render_recommendation_card(rec)
