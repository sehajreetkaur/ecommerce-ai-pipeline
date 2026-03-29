from unittest.mock import patch, MagicMock
from src.genai.sentiment import analyze_sentiment

MOCK_RESPONSE = '{"sentiment": "positive", "confidence": 0.95, "key_themes": ["delivery", "quality"], "summary": "Great product and fast delivery."}'


def test_analyze_sentiment_positive():
    mock_message = MagicMock()
    mock_message.content = [MagicMock(text=MOCK_RESPONSE)]

    with patch("src.genai.sentiment.client") as mock_client:
        mock_client.messages.create.return_value = mock_message
        result = analyze_sentiment("Great product!", 5)

    assert result["sentiment"] == "positive"
    assert result["confidence"] > 0.5
