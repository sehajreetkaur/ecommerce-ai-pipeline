import plotly.express as px
import pandas as pd


def revenue_trend_chart(df: pd.DataFrame):
    return px.line(
        df,
        x="month",
        y="total_revenue",
        title="Monthly Revenue",
        labels={"month": "Month", "total_revenue": "Revenue ($)"},
    )


def orders_trend_chart(df: pd.DataFrame):
    return px.bar(
        df,
        x="month",
        y="total_orders",
        title="Monthly Orders",
        labels={"month": "Month", "total_orders": "Orders"},
    )
