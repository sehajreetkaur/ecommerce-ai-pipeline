with seller_perf as (
    select * from {{ ref('int_seller_performance') }}
)

select
    seller_id,
    seller_city,
    seller_state,
    total_orders,
    total_revenue,
    round(avg_review_score::numeric, 2) as avg_review_score,
    rank() over (order by total_revenue desc) as revenue_rank,
    rank() over (order by avg_review_score desc) as rating_rank
from seller_perf
