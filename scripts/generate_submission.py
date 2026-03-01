import pandas as pd
from src.recommender.pipeline import RecommendationPipeline

EVAL_PATH = "data/eval/Gen_AI_Dataset.xlsx"
OUTPUT_PATH = "submission.csv"
TOP_K = 10

def main():
    print("Loading evaluation queries...")
    eval_df = pd.read_excel(EVAL_PATH)

    pipeline = RecommendationPipeline()

    rows = []

    for query in eval_df["Query"].unique():
        print(f"Processing: {query}")
        recommendations = pipeline.recommend(query, k=TOP_K)

        for rec in recommendations:
            rows.append({
                "Query": query,
                "Assessment_url": rec["url"]
            })

    submission_df = pd.DataFrame(rows)

    submission_df.to_csv(OUTPUT_PATH, index=False)

    print("Submission file generated successfully.")
    print(f"Total rows: {len(submission_df)}")

if __name__ == "__main__":
    main()