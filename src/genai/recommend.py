import os
import json
import anthropic
from dotenv import load_dotenv
from src.genai.prompt_templates import RECOMMENDATION_PROMPT

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def get_recommendations(customer_profile: dict, candidate_products: list) -> list:
    """Generate personalized product recommendations using Claude."""
    prompt = RECOMMENDATION_PROMPT.format(
        segment=customer_profile.get("segment", "new"),
        past_purchases=", ".join(customer_profile.get("past_purchases", [])),
        order_count=customer_profile.get("order_count", 0),
        lifetime_value=customer_profile.get("lifetime_value", 0.0),
        candidate_products=json.dumps(candidate_products, indent=2),
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    content = message.content[0].text
    return json.loads(content)
