# Ecommerce AI Pipeline — dbt Overview

## Project Structure

### Staging
Raw source data cleaned and type-cast. One model per source table.

### Intermediate
Business logic combining staging models:
- `int_customer_orders` — orders enriched with customer and payment data
- `int_product_performance` — revenue and order counts per product
- `int_seller_performance` — seller metrics with review scores
- `int_review_sentiment` — rule-based sentiment labels on reviews
- `int_customer_segments` — RFM-style customer segmentation

### Marts
Final analytics-ready tables consumed by Streamlit dashboards:
- `mart_customer_summary` — customer lifetime value and segments
- `mart_product_affinity` — co-purchase product pairs
- `mart_top_products` — ranked products by revenue and orders
- `mart_seller_scorecard` — seller rankings by revenue and rating
- `mart_revenue_trends` — monthly revenue and order trends
