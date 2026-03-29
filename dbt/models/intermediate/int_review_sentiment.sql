with reviews as (
    select * from {{ ref('stg_reviews') }}
)

select
    review_id,
    order_id,
    review_score,
    review_comment_message,
    review_creation_date,
    case
        when review_score >= 4 then 'positive'
        when review_score = 3 then 'neutral'
        else 'negative'
    end as sentiment_label
from reviews
