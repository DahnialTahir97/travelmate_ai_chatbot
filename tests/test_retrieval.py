from src.retrieval import TravelRetriever


def test_dataset_has_at_least_30_pairs():
    retriever = TravelRetriever()
    assert len(retriever.data) >= 30


def test_retrieval_finds_langkawi_topic():
    retriever = TravelRetriever()
    results = retriever.search("What beaches can I visit in Langkawi?")
    assert results
    assert (
        "Langkawi" in results[0]["question"]
        or "Langkawi" in results[0]["answer"]
    )


def test_empty_question_returns_no_results():
    retriever = TravelRetriever()
    assert retriever.search("   ") == []
