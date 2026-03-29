with source as (
    select * from {{ source('raw', 'olist_orders') }}
)

select
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp::timestamp as order_purchase_at,
    order_approved_at::timestamp,
    order_delivered_carrier_date::timestamp,
    order_delivered_customer_date::timestamp,
    order_estimated_delivery_date::timestamp
from source
