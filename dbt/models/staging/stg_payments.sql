with source as (
    select * from {{ source('raw', 'olist_order_payments') }}
)

select
    order_id,
    payment_sequential::int,
    payment_type,
    payment_installments::int,
    payment_value::numeric
from source
