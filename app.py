from fastapi import FastAPI
from pydantic import BaseModel
from src.recommender.pipeline import RecommendationPipeline

app = FastAPI(title="SHL Assessment Recommendation API")

pipeline = None  # initialize later


@app.on_event("startup")
def load_pipeline():
    global pipeline
    pipeline = RecommendationPipeline()
    print("Pipeline loaded successfully")


class QueryRequest(BaseModel):
    query: str


@app.post("/recommend")
def recommend(request: QueryRequest):
    results = pipeline.recommend(request.query, k=10)
    return {"recommendations": results}


@app.get("/")
def health():
    return {"status": "running"}