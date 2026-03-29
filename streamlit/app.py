import streamlit as st

st.set_page_config(
    page_title="Ecommerce AI Pipeline",
    page_icon="🛒",
    layout="wide",
)

st.title("Ecommerce AI Pipeline Dashboard")
st.markdown(
    """
    Welcome to the Ecommerce AI Pipeline dashboard.

    Use the sidebar to navigate between pages:
    - **Overview** — Sales & revenue trends
    - **Customer Insights** — Segmentation and lifetime value
    - **Product Performance** — Top products and category analysis
    - **Seller Scorecard** — Seller rankings and ratings
    - **Sentiment Analysis** — Review sentiment powered by AI
    - **AI Recommendations** — Personalized product recommendations
    """
)
