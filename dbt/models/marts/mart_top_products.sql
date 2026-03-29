with product_perf as (
    select * from {{ ref('int_product_performance') }}
)

select
    product_id,
    product_category_name,
    total_orders,
    total_revenue,
    avg_price,
    rank() over (order by total_revenue desc) as revenue_rank,
    rank() over (order by total_orders desc) as order_rank
from product_perf
