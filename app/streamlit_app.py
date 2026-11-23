import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import streamlit as st
from dotenv import load_dotenv
from src.chatbot import answer_question
from src.retrieval import TravelRetriever

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

st.set_page_config(page_title="TravelMate AI", page_icon="🧭", layout="centered")
st.title("🧭 TravelMate AI")
st.caption("Your Malaysia Travel & Tourism Assistant")
st.write(
    "Ask about attractions, activities, transport and practical travel tips "
    "in Malaysia."
)

with st.sidebar:
    st.header("Explore destinations")
    st.markdown(
        "- Kuala Lumpur\n- Melaka\n- Penang\n- Langkawi\n- Cameron Highlands"
    )
    st.divider()
    st.caption(
        "TravelMate provides general information, not live booking, ticketing "
        "or emergency services."
    )
    demo_mode = st.toggle(
        "Dataset-only demo mode",
        value=not bool(os.getenv("GEMINI_API_KEY")),
    )
    if not demo_mode and not os.getenv("GEMINI_API_KEY"):
        st.warning("Add GEMINI_API_KEY to .env to enable Gemini responses.")


@st.cache_resource
def load_retriever():
    return TravelRetriever()


retriever = load_retriever()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! I'm TravelMate. Where in Malaysia would you like to explore?"
            ),
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask TravelMate about a destination..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Finding travel information..."):
            try:
                response, matches = answer_question(
                    prompt, retriever, use_llm=not demo_mode
                )
                st.markdown(response)
                if matches:
                    with st.expander("Dataset references used"):
                        for item in matches:
                            st.caption(f"Match score: {item['score']:.2f}")
                            st.markdown(f"**{item['question']}**")
                            st.write(item["answer"])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
            except Exception as exc:
                st.error(str(exc))
                st.info(
                    "Switch on Dataset-only demo mode or configure your Gemini API key."
                )
