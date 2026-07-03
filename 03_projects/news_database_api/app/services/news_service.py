from app.database import get_connection
import os
import requests
from app.utils.helpers import rows_to_news

def get_all_news():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM news")
    rows = cursor.fetchall()

    news = rows_to_news(rows)

    return {
    "total": len(news),
    "news": news
}


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

 news = rows_to_news(rows)

 return {
    "total": len(news),
    "news": news
}


# -----------------------------

# Filter By Source

# -----------------------------


def news_by_source(source_name: str):


 conn = get_connection()
 cursor = conn.cursor()

 cursor.execute(
    "SELECT * FROM news WHERE source = ?",
    (source_name,)
)
 rows = cursor.fetchall()

 news = rows_to_news(rows)

 return {
    "total": len(news),
    "news": news
}

# -----------------------------

# Add News

# -----------------------------


def add_news(title: str, source: str, published: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO news (title, source, published)
        VALUES (?, ?, ?)
    """, (
        title,
        source,
        published
    ))

    conn.commit()
    conn.close()

    return {
        "message": "News added successfully"
    }