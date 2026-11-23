"""Google Gemini integration. API keys are read from environment only."""
import os
from google import genai

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def generate_answer(question, retrieved_context, api_key=None):
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured. Add it to your local .env file."
        )

    client = genai.Client(api_key=key)
    context = "\n\n".join(
        f"Reference Q: {item['question']}\nReference A: {item['answer']}"
        for item in retrieved_context
    )
    prompt = f"""You are TravelMate, a careful Malaysia travel information assistant.
Answer the user's question clearly and helpfully.
Use the supplied reference context as your primary source. Do not invent opening hours,
live prices, schedules, availability, visa decisions, or real-time conditions.
If the context is insufficient, say so and direct the user to an official source.
For safety or emergencies, advise following local authorities.
You provide information only; you do not make bookings.

REFERENCE CONTEXT:
{context or "No relevant reference found."}

USER QUESTION:
{question}
"""
    response = client.models.generate_content(
        model=DEFAULT_MODEL,
        contents=prompt,
    )
    answer = getattr(response, "text", None)
    if not answer:
        raise RuntimeError("The model returned an empty response. Please try again.")
    return answer.strip()
