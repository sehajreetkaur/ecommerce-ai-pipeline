with orders as (
    select * from {{ ref('int_customer_orders') }}
    where order_status = 'delivered'
)

select
    date_trunc('month', order_purchase_at) as month,
    count(distinct order_id) as total_orders,
    sum(order_value) as total_revenue,
    avg(order_value) as avg_order_value,
    count(distinct customer_unique_id) as unique_customers
from orders
group by 1
order by 1
