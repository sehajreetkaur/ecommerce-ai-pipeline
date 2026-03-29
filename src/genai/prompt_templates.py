RECOMMENDATION_PROMPT = """You are an ecommerce recommendation assistant.

Customer profile:
- Segment: {segment}
- Past purchases: {past_purchases}
- Total orders: {order_count}
- Lifetime value: ${lifetime_value:.2f}

Available products to recommend:
{candidate_products}

Provide 3 personalized product recommendations with a brief explanation for each.
Format as a JSON list with keys: product_id, product_name, reason.
"""

SENTIMENT_PROMPT = """Analyze the sentiment of the following customer review.

Review: "{review_text}"
Star rating: {review_score}/5

Respond with a JSON object containing:
- sentiment: "positive", "neutral", or "negative"
- confidence: float between 0 and 1
- key_themes: list of up to 3 themes mentioned
- summary: one sentence summary
"""

EXPLANATION_PROMPT = """Explain why these products are recommended for this customer.

Customer segment: {segment}
Recommended products: {products}
Purchase history summary: {history_summary}

Write a friendly, concise explanation in 2-3 sentences suitable for displaying in a dashboard.
"""
