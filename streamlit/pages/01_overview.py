import streamlit as st
import pandas as pd
from src.db.db_connect import get_engine
from components.charts import revenue_trend_chart
from components.metrics import kpi_row

st.set_page_config(page_title="Overview", layout="wide")
st.title("Sales & Revenue Overview")

engine = get_engine()

df = pd.read_sql("select * from mart_revenue_trends order by month", engine)

kpi_row(
    total_revenue=df["total_revenue"].sum(),
    total_orders=df["total_orders"].sum(),
    avg_order_value=df["avg_order_value"].mean(),
    unique_customers=df["unique_customers"].sum(),
)

st.plotly_chart(revenue_trend_chart(df), use_container_width=True)
