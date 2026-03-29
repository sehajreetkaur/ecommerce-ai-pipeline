with source as (
    select * from {{ source('raw', 'olist_order_reviews') }}
)

select
    review_id,
    order_id,
    review_score::int,
    review_comment_title,
    review_comment_message,
    review_creation_date::timestamp,
    review_answer_timestamp::timestamp
from source
