import pickle
import re
from rank_bm25 import BM25Okapi

class BM25Retriever:

    def __init__(self, catalog_path="data/embeddings/catalog.pkl"):
        with open(catalog_path, "rb") as f:
            self.df = pickle.load(f)

        # Combine name + description for better keyword coverage
        self.documents = (
            self.df["name"].fillna("") + " " +
            self.df["description"].fillna("")
        ).tolist()

        # Basic tokenization
        self.tokenized_corpus = [
            self._tokenize(doc) for doc in self.documents
        ]

        self.bm25 = BM25Okapi(self.tokenized_corpus)

    def _tokenize(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        return text.split()

    def search(self, query, k=20):
        tokenized_query = self._tokenize(query)
        scores = self.bm25.get_scores(tokenized_query)

        # Get top-k indices
        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:k]

        return ranked_indices, scores