with customer_orders as (
    select * from {{ ref('int_customer_orders') }}
),

aggregated as (
    select
        customer_unique_id,
        count(distinct order_id) as order_count,
        sum(order_value) as lifetime_value,
        max(order_purchase_at) as last_order_date
    from customer_orders
    group by customer_unique_id
)

select
    customer_unique_id,
    order_count,
    lifetime_value,
    last_order_date,
    case
        when order_count >= 5 then 'champion'
        when order_count >= 3 then 'loyal'
        when order_count = 2 then 'potential'
        else 'new'
    end as segment
from aggregated
