with segments as (
    select * from {{ ref('int_customer_segments') }}
)

select
    customer_unique_id,
    segment,
    order_count,
    lifetime_value,
    last_order_date,
    round(lifetime_value / nullif(order_count, 0), 2) as avg_order_value
from segments
