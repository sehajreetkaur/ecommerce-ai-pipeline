import streamlit as st
from src.utils.helpers import format_currency


def kpi_row(total_revenue: float, total_orders: int, avg_order_value: float, unique_customers: int):
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", format_currency(total_revenue))
    col2.metric("Total Orders", f"{int(total_orders):,}")
    col3.metric("Avg Order Value", format_currency(avg_order_value))
    col4.metric("Unique Customers", f"{int(unique_customers):,}")
