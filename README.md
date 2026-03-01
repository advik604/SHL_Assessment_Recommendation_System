# SHL Assessment Recommendation System (Submission Ready)

## Full Pipeline
1. Crawl SHL catalog (>=377 Individual Test Solutions)
2. Build structured dataset
3. Generate embeddings (Sentence Transformers)
4. Store FAISS index
5. Run evaluation (Mean Recall@10)
6. Generate submission.csv
7. Run API + Frontend

---

## 1️⃣ Crawl Data
python scripts/run_crawler.py

## 2️⃣ Build Embedding Index
python scripts/build_index.py

## 3️⃣ Evaluate
python scripts/evaluate.py

## 4️⃣ Generate Test Predictions
python scripts/generate_predictions.py

## 5️⃣ Run API
uvicorn src.api.main:app --host 0.0.0.0 --port 8000

## 6️⃣ Run Frontend
streamlit run src/frontend/app.py

---

API Endpoints:
GET /health
POST /recommend
{
  "query": "Need Java developer with teamwork skills"
}