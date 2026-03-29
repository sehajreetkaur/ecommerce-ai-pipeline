import pandas as pd


def format_currency(value: float) -> str:
    return f"${value:,.2f}"


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    if denominator == 0:
        return default
    return numerator / denominator


def truncate_text(text: str, max_length: int = 100) -> str:
    if not text:
        return ""
    return text if len(text) <= max_length else text[:max_length] + "..."


def df_to_records(df: pd.DataFrame) -> list[dict]:
    return df.to_dict(orient="records")
