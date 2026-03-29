with items as (
    select * from {{ ref('stg_order_items') }}
),

products as (
    select * from {{ ref('stg_products') }}
),

orders as (
    select order_id, order_status from {{ ref('stg_orders') }}
)

select
    i.product_id,
    p.product_category_name,
    count(distinct i.order_id) as total_orders,
    sum(i.price) as total_revenue,
    avg(i.price) as avg_price,
    sum(i.freight_value) as total_freight
from items i
left join products p using (product_id)
left join orders o using (order_id)
where o.order_status = 'delivered'
group by i.product_id, p.product_category_name
