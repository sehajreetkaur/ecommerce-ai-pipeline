from unittest.mock import patch, MagicMock
from src.genai.recommend import get_recommendations

MOCK_CUSTOMER = {
    "segment": "loyal",
    "past_purchases": ["product_a", "product_b"],
    "order_count": 3,
    "lifetime_value": 250.0,
}

MOCK_PRODUCTS = [
    {"product_id": "p1", "product_category_name": "electronics", "avg_price": 99.0},
]

MOCK_RESPONSE = '[{"product_id": "p1", "product_name": "Widget", "reason": "Popular in your category"}]'


def test_get_recommendations_returns_list():
    mock_message = MagicMock()
    mock_message.content = [MagicMock(text=MOCK_RESPONSE)]

    with patch("src.genai.recommend.client") as mock_client:
        mock_client.messages.create.return_value = mock_message
        result = get_recommendations(MOCK_CUSTOMER, MOCK_PRODUCTS)

    assert isinstance(result, list)
    assert result[0]["product_id"] == "p1"
