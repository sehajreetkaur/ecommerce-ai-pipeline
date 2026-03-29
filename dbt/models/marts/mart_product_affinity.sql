with items as (
    select * from {{ ref('stg_order_items') }}
)

select
    a.product_id as product_a,
    b.product_id as product_b,
    count(*) as co_purchase_count
from items a
join items b
    on a.order_id = b.order_id
    and a.product_id < b.product_id
group by a.product_id, b.product_id
having count(*) > 1
order by co_purchase_count desc
