import sqlite3
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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

        cursor.execute("""
            INSERT INTO news
            (title, source, published)
            VALUES (?, ?, ?)
        """, (
            article["title"],
            article["source"]["name"],
            article["publishedAt"]
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

