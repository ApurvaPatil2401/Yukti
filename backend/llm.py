import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama-3.1-8b-instant"


def generate_concept_question(problem, concept):
    prompt = f"""
You are Yukti, a strict but supportive AI coding mentor.

Ask ONE clear, concise conceptual question about {concept}
related to this problem:

{problem}

Rules:
- Ask only ONE focused question.
- Do NOT combine multiple topics.
- Do NOT ramble.
- Do NOT give code.
- Keep it under 2 sentences.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


def evaluate_answer(concept, user_answer):
    prompt = f"""
    You are evaluating a student's explanation of the concept: {concept}.

    Student answer:
    {user_answer}

    If the student shows correct conceptual understanding, respond ONLY with YES.
    If the explanation is weak or incorrect, respond ONLY with NO.
    """

    response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content.strip()
    return "YES" in result.upper()

def generate_hint(concept, user_answer):
    prompt = f"""
You are a strict but helpful programming mentor.

The concept being tested is: {concept}

The student gave this explanation:
{user_answer}

The explanation is weak.

Give a short hint (2–3 sentences max) that helps the student think deeper about the concept.
Do NOT give the full answer.
Do NOT give code.
Only provide a hint.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()