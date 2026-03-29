import streamlit as st


def render_recommendation_card(rec: dict):
    with st.container():
        st.markdown(f"### {rec.get('product_name', rec.get('product_id', 'Product'))}")
        st.caption(f"Product ID: {rec.get('product_id', 'N/A')}")
        st.write(rec.get("reason", ""))
        st.divider()
