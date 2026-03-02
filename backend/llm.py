import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama-3.1-8b-instant"


def generate_hint(concept, user_answer):
    prompt = f"""
You are Yukti, a strict but supportive coding mentor.

The student is being tested on: {concept}

Student answer:
{user_answer}

The answer is incomplete.

Give a short, precise hint (max 2 sentences).
Do NOT give the full answer.
Do NOT give code.
Be technical and direct.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()