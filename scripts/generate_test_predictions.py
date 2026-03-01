import pandas as pd
from src.recommender.pipeline import RecommendationPipeline

pipeline = RecommendationPipeline()

df = pd.read_excel("data/eval/Gen_AI_Dataset.xlsx", sheet_name="Test-Set")

results = []

for query in df["Query"]:
    preds = pipeline.recommend(query, k=10)
    pred_urls = [p["url"] for p in preds]
    
    results.append({
        "query": query,
        "predictions": ", ".join(pred_urls)
    })

submission = pd.DataFrame(results)
submission.to_csv("final_test_predictions.csv", index=False)

print("CSV generated successfully!")