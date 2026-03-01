import pandas as pd
import numpy as np
import faiss
import pickle
from src.embeddings.embedder import Embedder

df = pd.read_csv("data/processed/catalog.csv")

embedder = Embedder()
embeddings = embedder.encode(df["name"].tolist())

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings).astype("float32"))

faiss.write_index(index, "data/embeddings/faiss.index")

with open("data/embeddings/catalog.pkl", "wb") as f:
    pickle.dump(df, f)

print("FAISS index built successfully.")