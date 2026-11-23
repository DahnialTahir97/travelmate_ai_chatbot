"""Lightweight TF-IDF retrieval over the TravelMate custom Q&A dataset."""
from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DEFAULT_DATASET = Path(__file__).resolve().parents[1] / "data" / "travel_dataset.csv"


class TravelRetriever:
    def __init__(self, dataset_path=DEFAULT_DATASET):
        self.data = pd.read_csv(dataset_path).fillna("")
        if not {"Question", "Answer"}.issubset(self.data.columns):
            raise ValueError("Dataset must contain Question and Answer columns.")
        if len(self.data) < 30:
            raise ValueError("Dataset must contain at least 30 Q&A pairs.")
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2), stop_words="english"
        )
        self.matrix = self.vectorizer.fit_transform(
            self.data["Question"].astype(str)
        )

    def search(self, question, top_k=3):
        question = (question or "").strip()
        if not question:
            return []
        query = self.vectorizer.transform([question])
        scores = cosine_similarity(query, self.matrix).ravel()
        indexes = scores.argsort()[::-1][:top_k]
        return [
            {
                "question": str(self.data.iloc[i]["Question"]),
                "answer": str(self.data.iloc[i]["Answer"]),
                "score": float(scores[i]),
            }
            for i in indexes
            if scores[i] > 0
        ]
