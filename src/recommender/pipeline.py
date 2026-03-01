import faiss
import pickle
import numpy as np
import pandas as pd
from src.embeddings.embedder import Embedder
from src.utils.config import settings
from src.recommender.bm25_retriever import BM25Retriever


def extract_slug(url):
    return url.strip().lower().rstrip("/").split("/")[-1]


def build_slug_boost_map(excel_path="data/eval/Gen_AI_Dataset.xlsx"):
    train = pd.read_excel(excel_path, sheet_name="Train-Set")

    role_slug_map = {}

    role_keywords = [
        "consultant",
        "developer",
        "engineer",
        "manager",
        "analyst",
        "sales"
    ]

    for _, row in train.iterrows():
        query = row["Query"].lower()
        slug = extract_slug(row["Assessment_url"])

        for role in role_keywords:
            if role in query:
                if role not in role_slug_map:
                    role_slug_map[role] = {}
                role_slug_map[role][slug] = role_slug_map[role].get(slug, 0) + 1

    return role_slug_map


class RecommendationPipeline:

    def __init__(self):
        # Dense embedder
        self.embedder = Embedder()

        # Load FAISS index
        self.index = faiss.read_index("data/embeddings/faiss.index")

        # Load catalog dataframe
        with open("data/embeddings/catalog.pkl", "rb") as f:
            self.df = pickle.load(f)

        # Sparse retriever
        self.bm25 = BM25Retriever()

        # Training-based boost map
        self.slug_boost_map = build_slug_boost_map()

    def _clean_query(self, query: str) -> str:
        query = query.lower()

        stop_sections = [
            "about us",
            "what shl can offer you",
            "shl is an equal opportunity employer"
        ]

        for section in stop_sections:
            if section in query:
                query = query.split(section)[0]

        query = query.replace("#", " ")

        return query.strip()

    def recommend(self, query, k=settings.TOP_K):

        # -------- Clean Query --------
        query = self._clean_query(query)

        # -------- Dense Retrieval (TOP 200) --------
        query_vec = self.embedder.encode([query])
        D, I = self.index.search(
            np.array(query_vec).astype("float32"),
            200
        )
        dense_ranked = list(I[0])

        # -------- Sparse Retrieval (TOP 200) --------
        sparse_indices, _ = self.bm25.search(query, k=200)
        sparse_ranked = list(sparse_indices)

        # -------- Reciprocal Rank Fusion --------
        def rrf_score(rank, k=60):
            return 1 / (k + rank)

        final_scores = {}

        # Dense contribution
        for rank, idx in enumerate(dense_ranked):
            final_scores[idx] = final_scores.get(idx, 0) + rrf_score(rank)

        # Sparse contribution
        for rank, idx in enumerate(sparse_ranked):
            final_scores[idx] = final_scores.get(idx, 0) + rrf_score(rank)

        # -------- Training-Based Boost --------
        query_lower = query.lower()

        for role, slug_counts in self.slug_boost_map.items():
            if role in query_lower:
                for idx, row in self.df.iterrows():
                    slug = extract_slug(row["url"])
                    if slug in slug_counts:
                        final_scores[idx] = final_scores.get(idx, 0) + 0.5

        # -------- Final Ranking --------
        ranked = sorted(
            final_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        top_indices = [idx for idx, _ in ranked[:k]]

        return self.df.iloc[top_indices][["name", "url"]].to_dict(
            orient="records"
        )