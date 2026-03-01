
# SHL Assessment Recommendation System

This project is a recommendation system that suggests relevant SHL assessments based on a job description or free-text query.

The goal is to take a user query (for example, a job description for a Java Developer or Data Analyst) and return the most suitable SHL assessment URLs in ranked order.

The system was built as part of an assessment task and includes:

* Model training and evaluation
* Hybrid retrieval pipeline
* Performance optimization
* API deployment
* Web frontend
* Test set prediction generation

---

## 🔍 Problem Overview

Given:

* A catalog of SHL assessments (name, URL, description)
* A labeled training dataset (query → relevant assessment URLs)

Build a system that:

1. Recommends top 10 relevant assessments for any input query
2. Maximizes Recall@10 on the training set
3. Exposes a public API endpoint
4. Provides a simple web interface
5. Generates predictions for the unlabeled test set

---

## 🧠 Approach

### 1. Data Processing

* Cleaned and normalized catalog text
* Combined assessment name and description
* Prepared slug mappings for evaluation

### 2. Hybrid Retrieval System

The final pipeline uses a combination of:

* **Dense embeddings (Sentence Transformers)**
* **FAISS similarity search**
* **BM25 keyword matching**
* **Score fusion for ranking**
* **Training-based slug boosting**

Pure semantic similarity was not sufficient, so lexical matching was combined with embeddings to improve recall.

---

## 📈 Evaluation

Metric used: **Recall@10**

Initial performance (baseline embedding only):

* Very low recall

After introducing hybrid retrieval and boosting:

* Mean Recall@10 improved significantly (~0.70+)

Evaluation script is included in the repository.

---

## 🏗️ Project Structure

<pre class="overflow-visible! px-0!" data-start="1973" data-end="2112"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>src/</span><br/><span>  recommender/</span><br/><span>    pipeline.py</span><br/><span>    training_boost.py</span><br/><span>    ...</span><br/><br/><span>app.py</span><br/><span>requirements.txt</span><br/><span>generate_test_predictions.py</span><br/><span>evaluate.py</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

* `pipeline.py` → Main recommendation logic
* `app.py` → FastAPI endpoint
* `evaluate.py` → Recall@10 evaluation
* `generate_test_predictions.py` → Creates final submission CSV

---

## 🚀 Running Locally

### 1. Install dependencies

<pre class="overflow-visible! px-0!" data-start="2357" data-end="2400"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>pip install </span><span class="ͼf">-r</span><span> requirements.txt</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### 2. Run API

<pre class="overflow-visible! px-0!" data-start="2418" data-end="2454"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>uvicorn app:app </span><span class="ͼf">--reload</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

API will be available at:

<pre class="overflow-visible! px-0!" data-start="2483" data-end="2517"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>http://127.0.0.1:8000/docs</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Test the `/recommend` endpoint using Swagger UI.

---

## 🌐 Deployment

The API is deployed on Render and exposes a POST endpoint:

<pre class="overflow-visible! px-0!" data-start="2652" data-end="2670"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>/recommend</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Request format:

<pre class="overflow-visible! px-0!" data-start="2689" data-end="2737"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>{</span><br/><span>  "query": </span><span class="ͼc">"Java developer test"</span><br/><span>}</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Response:

<pre class="overflow-visible! px-0!" data-start="2750" data-end="2829"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>{</span><br/><span>  "recommendations": [</span><br/><span></span><span class="ͼc">"https://..."</span><span>,</span><br/><span></span><span class="ͼc">"https://..."</span><br/><span>  ]</span><br/><span>}</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

A simple web frontend is also deployed to test the system interactively.

---

## 📄 Test Set Predictions

Final predictions for the unlabeled dataset are generated as a CSV file with:

* Column 1: `query`
* Column 2: `predictions` (comma-separated URLs)

Format matches the specification in the assignment PDF.

---
