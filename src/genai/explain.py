import os
import anthropic
from dotenv import load_dotenv
from src.genai.prompt_templates import EXPLANATION_PROMPT

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def generate_explanation(segment: str, products: list, history_summary: str) -> str:
    """Generate a natural language explanation for recommendations."""
    prompt = EXPLANATION_PROMPT.format(
        segment=segment,
        products=", ".join(products),
        history_summary=history_summary,
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )

    return message.content[0].text.strip()
