select order_id
from {{ ref('int_customer_orders') }}
where order_value < 0
