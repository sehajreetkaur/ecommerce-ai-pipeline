import os
import json
import anthropic
from dotenv import load_dotenv
from src.genai.prompt_templates import SENTIMENT_PROMPT

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def analyze_sentiment(review_text: str, review_score: int) -> dict:
    """Analyze sentiment of a customer review using Claude."""
    prompt = SENTIMENT_PROMPT.format(
        review_text=review_text,
        review_score=review_score,
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )

    content = message.content[0].text
    return json.loads(content)


def batch_analyze(reviews: list[dict]) -> list[dict]:
    """Run sentiment analysis on a list of review dicts with keys: review_text, review_score."""
    results = []
    for review in reviews:
        result = analyze_sentiment(review["review_text"], review["review_score"])
        result["review_id"] = review.get("review_id")
        results.append(result)
    return results
