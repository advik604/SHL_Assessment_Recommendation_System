from fastapi import FastAPI
from pydantic import BaseModel
from src.recommender.pipeline import RecommendationPipeline

app = FastAPI()
pipeline = RecommendationPipeline()

class QueryRequest(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend(request: QueryRequest):
    results = pipeline.recommend(request.query)
    return {"recommendations": results}