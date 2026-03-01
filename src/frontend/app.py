import streamlit as st
import requests

st.title("SHL Assessment Recommendation System")

query = st.text_area("Enter Job Description or Query")

if st.button("Recommend"):
    response = requests.post(
        "http://localhost:8000/recommend",
        json={"query": query}
    )
    results = response.json()["recommendations"]

    for r in results:
        st.write(f"### {r['name']}")
        st.write(r["url"])