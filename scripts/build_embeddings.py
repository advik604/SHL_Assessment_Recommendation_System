import pandas as pd
import numpy as np
import faiss
import pickle
import os

from src.embeddings.embedder import Embedder

DATA_PATH = "data/raw/assessments.csv"
EMBEDDING_DIR = "data/embeddings"

os.makedirs(EMBEDDING_DIR, exist_ok=True)

def main():
    print("Loading dataset...")
    df = pd.read_csv(DATA_PATH)

    print(f"Total products: {len(df)}")

    embedder = Embedder()

    print("Generating embeddings...")
    texts = (df["name"] + ". " + df["description"]).fillna("").tolist()

    embeddings = embedder.encode(texts)

    embeddings = np.array(embeddings).astype("float32")

    print("Building FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    print("Saving index...")
    faiss.write_index(index, f"{EMBEDDING_DIR}/faiss.index")

    print("Saving catalog...")
    with open(f"{EMBEDDING_DIR}/catalog.pkl", "wb") as f:
        pickle.dump(df, f)

    print("Done.")
    print(f"Indexed {index.ntotal} products.")

if __name__ == "__main__":
    main()