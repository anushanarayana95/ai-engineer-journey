import sqlite3
import requests
from fastapi import FastAPI
app = FastAPI()
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

DB_NAME = "news.db"

# -----------------------------

# Database Connection

# -----------------------------

def get_connection():
 conn = sqlite3.connect(DB_NAME)
 conn.row_factory = sqlite3.Row
 return conn

# -----------------------------

# Pydantic Model

# -----------------------------

class NewsItem(BaseModel):
 title: str
 source: str
 published: str

# -----------------------------

# Home Endpoint

# -----------------------------

@app.get("/")
def home():
 return {
"message": "News API is running",
"version": "1.0"
}

# -----------------------------

# Get All News

# -----------------------------

@app.get("/news")
def get_news():


 conn = get_connection()
 cursor = conn.cursor()

 cursor.execute("SELECT * FROM news")
 rows = cursor.fetchall()

 news = []

 for row in rows:
    news.append({
        "title": row["title"],
        "source": row["source"],
        "published": row["published"]
    })

 conn.close()

 return {
    "total": len(news),
    "news": news
}


# -----------------------------

# Count News

# -----------------------------

@app.get("/news/count")
def count_news():


 conn = get_connection()
 cursor = conn.cursor()

 cursor.execute("SELECT COUNT(*) AS total FROM news")

 result = cursor.fetchone()

 conn.close()

 return {
    "total_news": result["total"]
}


# -----------------------------

# Latest 5 News

# -----------------------------

@app.get("/news/latest")
def latest_news():


 conn = get_connection()
 cursor = conn.cursor()

 cursor.execute("""
    SELECT *
    FROM news
    ORDER BY published DESC
    LIMIT 5
""")

 rows = cursor.fetchall()

 news = []

 for row in rows:
    news.append({
        "title": row["title"],
        "source": row["source"],
        "published": row["published"]
    })

 conn.close()

 return {
    "count": len(news),
    "news": news
}


# -----------------------------

# Filter By Source

# -----------------------------

@app.get("/news/source/{source_name}")
def news_by_source(source_name: str):


 conn = get_connection()
 cursor = conn.cursor()

 cursor.execute(
    "SELECT * FROM news WHERE source = ?",
    (source_name,)
)

 rows = cursor.fetchall()

 news = []

 for row in rows:
    news.append({
        "title": row["title"],
        "source": row["source"],
        "published": row["published"]
    })

 conn.close()

 return {
    "source": source_name,
    "count": len(news),
    "news": news
}


# -----------------------------

# Add News

# -----------------------------

@app.post("/news")
def add_news(item: NewsItem):


 conn = get_connection()
 cursor = conn.cursor()

 cursor.execute("""
    INSERT INTO news (title, source, published)
    VALUES (?, ?, ?)
""", (
    item.title,
    item.source,
    item.published
))

 conn.commit()
 conn.close()

 return {
    "message": "News added successfully"
}


# -----------------------------

# Update News

# -----------------------------

@app.put("/news/{title}")
def update_news(title: str, item: NewsItem):


 conn = get_connection()
 cursor = conn.cursor()

 cursor.execute("""
    UPDATE news
    SET source = ?, published = ?
    WHERE title = ?
""", (
    item.source,
    item.published,
    title
))

 conn.commit()
 conn.close()

 return {
    "message": "News updated successfully"
}


# -----------------------------

# Delete News

# -----------------------------

@app.delete("/news/{title}")
def delete_news(title: str):


 conn = get_connection()
 cursor = conn.cursor()

 cursor.execute(
    "DELETE FROM news WHERE title = ?",
    (title,)
)

 conn.commit()
 conn.close()

 return {
    "message": f"Deleted news with title {title}"
}


# -----------------------------

@app.delete("/news/fake/string")
def delete_fake_news():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM news WHERE title = 'string'"
    )

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return {
        "deleted": deleted
    }

# Sync News From NewsAPI

# -----------------------------

API_KEY = "8b390caa5b8341729ba9e2b87e82b1c9"

@app.get("/sync-news")
def sync_news():


 url = (
    f"https://newsapi.org/v2/top-headlines"
    f"?country=us&apiKey={API_KEY}"
)

 response = requests.get(url)
 data = response.json()

 articles = data["articles"]

 conn = get_connection()
 cursor = conn.cursor()

 inserted = 0
 skipped = 0

 for article in articles:

    title = article["title"]

    cursor.execute(
        "SELECT COUNT(*) AS total FROM news WHERE title = ?",
        (title,)
    )

    exists = cursor.fetchone()["total"]
    
    if exists == 0:
     print("TITLE:", article.get("title"))
     print("DESCRIPTION:", article.get("description"))
     print("CONTENT:", article.get("content"))
     print("=" * 50)
     cursor.execute("""
INSERT INTO news
(title, source, published, content)
VALUES (?, ?, ?, ?)
""", (
    article["title"],
    article["source"]["name"],
    article["publishedAt"],
    article.get("content") or article.get("description") or ""
))

    inserted += 1

 else:
       skipped += 1
        

 conn.commit()
 conn.close()

 return {
    "message": "Sync completed",
    "inserted": inserted,
    "skipped": skipped
}

@app.post("/summarize-news/{title}")
def summarize_news(title: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM news WHERE title = ?",
        (title,)
    )

    article = cursor.fetchone()

    if not article:
        conn.close()
        return {"error": "Article not found"}
        print("CONTENT:")
        print(article["content"])
    prompt = f"""
Summarize this news article in 3-5 sentences.

Title:
{article['title']}

Source:
{article['source']}

Content:
{article['content']}

"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    summary = response.text
    cursor.execute("""
        UPDATE news
        SET summary = ?
        WHERE title = ?
    """, (
        summary,
        title
    ))

    conn.commit()
    conn.close()

    return {
        "title": title,
        "summary": summary
    }

# delete news
@app.delete("/news/all")
def delete_all_news():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM news")

    conn.commit()
    conn.close()

    return {"message": "All news deleted"}
#news check
@app.get("/news/check-latest")
def check_latest():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT title, content
    FROM news
    ORDER BY published DESC
    LIMIT 5
    """)

    rows = cursor.fetchall()


    conn.close()

    return [dict(row) for row in rows]

#new analyze
@app.post("/analyze-news/{title}")
def analyze_news(title: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM news WHERE title = ?",
        (title,)
    )

    article = cursor.fetchone()

    if not article:
        conn.close()
        return {"error": "Article not found"}

    content = article["content"]

    prompt_text = f"""
Analyze the following news article.

Title:
{article['title']}

Content:
{content}

Return exactly in this format:

SUMMARY:
<2-3 sentence summary>

CATEGORY:
<one category>

KEYWORDS:
<comma separated keywords>
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_text
    )

    result = response.text

    print(result)

    summary = result.split("CATEGORY:")[0]
    summary = summary.replace("SUMMARY:", "").strip()

    category = result.split("CATEGORY:")[1]
    category = category.split("KEYWORDS:")[0].strip()

    keywords = result.split("KEYWORDS:")[1].strip()

    cursor.execute("""
        UPDATE news
        SET summary = ?,
            category = ?,
            keywords = ?
        WHERE title = ?
    """, (
        summary,
        category,
        keywords,
        title
    ))

    conn.commit()
    conn.close()

    return {
        "title": title,
        "summary": summary,
        "category": category,
        "keywords": keywords
    }
@app.get("/analytics")
def analytics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM news
    """)

    total_articles = cursor.fetchone()[0]

    cursor.execute("""
    SELECT source, COUNT(*)
    FROM news
    GROUP BY source
    ORDER BY COUNT(*) DESC
    """)

    source_counts = {}

    for source, count in cursor.fetchall():
        source_counts[source] = count

    conn.close()

    return {
        "total_articles": total_articles,
        "sources": source_counts
    }
#-search--------------

@app.get("/search/{keyword}")
def search_news(keyword: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM news
        WHERE title LIKE ?
    """, (f"%{keyword}%",))

    results = cursor.fetchall()

    conn.close()

    return results

#latest news-----------------------

@app.get("/latest")
def latest_news():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM news
        ORDER BY published DESC
        LIMIT 10
    """)

    articles = cursor.fetchall()

    conn.close()

    return [dict(article) for article in articles]