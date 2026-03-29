with items as (
    select * from {{ ref('stg_order_items') }}
),

orders as (
    select * from {{ ref('stg_orders') }}
),

sellers as (
    select * from {{ ref('stg_sellers') }}
),

reviews as (
    select
        order_id,
        avg(review_score) as avg_review_score
    from {{ ref('stg_reviews') }}
    group by order_id
)

select
    i.seller_id,
    s.seller_city,
    s.seller_state,
    count(distinct i.order_id) as total_orders,
    sum(i.price) as total_revenue,
    avg(r.avg_review_score) as avg_review_score
from items i
left join sellers s using (seller_id)
left join orders o using (order_id)
left join reviews r using (order_id)
where o.order_status = 'delivered'
group by i.seller_id, s.seller_city, s.seller_state
