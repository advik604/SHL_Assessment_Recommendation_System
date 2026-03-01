import pandas as pd
from src.recommender.pipeline import RecommendationPipeline

pipeline = RecommendationPipeline()

test_df = pd.read_csv("data/test.csv")

rows = []

for _, row in test_df.iterrows():
    query = row["Query"]
    results = pipeline.recommend(query)

    for r in results:
        rows.append({
            "Query": query,
            "Assessment_url": r["url"]
        })

pd.DataFrame(rows).to_csv("submission.csv", index=False)
print("submission.csv generated successfully.")