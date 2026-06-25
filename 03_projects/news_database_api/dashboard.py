import pandas as pd
import streamlit as st
import requests

# -----------------------------

# Page Config

# -----------------------------

st.set_page_config(
page_title="News Intelligence Dashboard",
page_icon="📰",
layout="wide"
)

# -----------------------------

# Header

# -----------------------------

st.title("📰 News Intelligence Dashboard")
st.write("AI-Powered News Analytics Platform")

# -----------------------------

# Analytics Data

# -----------------------------

analytics_response = requests.get(
"http://127.0.0.1:8000/analytics"
)

data = analytics_response.json()

# -----------------------------

# Metrics Row

# -----------------------------

col1, col2 = st.columns(2)

with col1:
 st.metric(
"📄 Total Articles",
data["total_articles"]
)

with col2:
 st.metric(
"📰 News Sources",
len(data["sources"])
)

# -----------------------------

# Top Sources

# -----------------------------

st.divider()

st.subheader("📊 Top News Sources")

for source, count in list(data["sources"].items())[:10]:
 st.markdown(
f"**{source}** — {count} articles"
)

# -----------------------------

#----------------------------


st.divider()

st.subheader("📈 News Source Distribution")

chart_data = pd.DataFrame(
    {
        "Source": list(data["sources"].keys())[:10],
        "Articles": list(data["sources"].values())[:10]
    }
)

st.bar_chart(
    chart_data.set_index("Source")
)
# -----------------
# -----------------------------
# Search Section
# -----------------------------

st.divider()

st.subheader("🔍 Search News")

keyword = st.text_input("Enter a keyword")

if keyword:

    search_response = requests.get(
        f"http://127.0.0.1:8000/search/{keyword}"
    )

    results = search_response.json()

    st.success(
        f"Found {len(results)} articles"
    )

    for article in results:
        st.markdown(
            f"🔹 {article['title']}"
        )
 #------------------------

# Latest Articles

# -----------------------------
st.divider()

st.subheader("📰 Latest Articles")

latest_response = requests.get(
"http://127.0.0.1:8000/latest"
)

latest_articles = latest_response.json()

for article in latest_articles:
 st.markdown(
f"• {article['title']}"
)
 #------------------------------------

 #AI ANALYSIS
latest_response = requests.get(
    "http://127.0.0.1:8000/latest"
)

latest_articles = latest_response.json()
st.divider()

st.subheader("🤖 AI News Analysis")

article_titles = [
    article["title"]
    for article in latest_articles
]

article_title = st.selectbox(
    "Choose an Article",
    article_titles
)


if st.button("Analyze Article"):

    analyze_response = requests.post(
        f"http://127.0.0.1:8000/analyze-news/{article_title}"
    )

    st.write("Status Code:", analyze_response.status_code)
    st.write("Response:", analyze_response.text)

   

    

# Footer

# -----------------------------

st.divider()

st.caption(
"Built with FastAPI • SQLite • Gemini AI • Streamlit"
)
