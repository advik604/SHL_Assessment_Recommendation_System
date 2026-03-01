from fastapi import FastAPI
from pydantic import BaseModel
from src.recommender.pipeline import RecommendationPipeline

app = FastAPI(title="SHL Assessment Recommendation API")

pipeline = RecommendationPipeline()

class QueryRequest(BaseModel):
    query: str

@app.post("/recommend")
def recommend(request: QueryRequest):
    results = pipeline.recommend(request.query, k=10)
    return {"recommendations": results}