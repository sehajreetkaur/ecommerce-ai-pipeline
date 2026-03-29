with source as (
    select * from {{ source('raw', 'olist_order_items') }}
)

select
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date::timestamp,
    price::numeric,
    freight_value::numeric
from source
