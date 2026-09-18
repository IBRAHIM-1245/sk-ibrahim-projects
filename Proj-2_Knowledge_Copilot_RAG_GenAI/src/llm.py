from .openai_client import client
from .config import OPENAI_MODEL


def generate_response(prompt: str) -> str:
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt,
    )
    return response.output_text