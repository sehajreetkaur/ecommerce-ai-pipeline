with orders as (
    select * from {{ ref('stg_orders') }}
),

payments as (
    select
        order_id,
        sum(payment_value) as total_payment
    from {{ ref('stg_payments') }}
    group by order_id
),

customers as (
    select * from {{ ref('stg_customers') }}
)

select
    o.order_id,
    o.customer_id,
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,
    o.order_status,
    o.order_purchase_at,
    o.order_delivered_customer_date,
    coalesce(p.total_payment, 0) as order_value
from orders o
left join customers c using (customer_id)
left join payments p using (order_id)
