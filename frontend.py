import streamlit as st
import requests

API_URL = "https://shl-assessment-recommendation-system-92m0.onrender.com/recommend"

st.title("SHL Assessment Recommendation System")

query = st.text_area("Enter Job Description or Query")

if st.button("Get Recommendations"):
    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        response = requests.post(API_URL, json={"query": query})
        
        if response.status_code == 200:
            results = response.json()["recommendations"]
            
            st.subheader("Top Recommendations:")
            for r in results:
                st.write(f"**{r['name']}**")
                st.write(r['url'])
                st.write("---")
        else:
            st.error("Error fetching recommendations.")