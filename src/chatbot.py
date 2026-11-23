"""Application service joining retrieval and Gemini generation."""
from src.retrieval import TravelRetriever
from src.model import generate_answer


def answer_question(question, retriever=None, use_llm=True):
    retriever = retriever or TravelRetriever()
    matches = retriever.search(question, top_k=3)
    if use_llm:
        return generate_answer(question, matches), matches
    if not matches or matches[0]["score"] < 0.08:
        return (
            "I couldn't find a sufficiently relevant answer in the TravelMate "
            "dataset. Please try asking about Kuala Lumpur, Melaka, Penang, "
            "Langkawi or Cameron Highlands."
        ), matches
    return matches[0]["answer"], matches
