import pandas as pd
from src.recommender.pipeline import RecommendationPipeline
from src.evaluation.metrics import recall_at_k, mean_recall

TOP_K = 10
EVAL_PATH = "data/eval/Gen_AI_Dataset.xlsx"

pipeline = RecommendationPipeline()

print("Loading Train-Set...")
df = pd.read_excel(EVAL_PATH, sheet_name="Train-Set")

grouped = df.groupby("Query")["Assessment_url"].apply(list).reset_index()

scores = []

for _, row in grouped.iterrows():
    query = row["Query"]
    truth = row["Assessment_url"]

    preds = pipeline.recommend(query, k=TOP_K)
    pred_urls = [p["url"] for p in preds]

    score = recall_at_k(pred_urls, truth)
    scores.append(score)

    print(f"Query: {query}")
    print(f"Recall@{TOP_K}: {score:.4f}")
    print("----------------------")


print("\n======================")
print("Mean Recall@10:", mean_recall(scores))
print("======================")