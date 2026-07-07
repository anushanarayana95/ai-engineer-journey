from app.database import get_connection
from app.utils.helpers import rows_to_news
from fastapi import HTTPException

def get_all_news():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM news")
    rows = cursor.fetchall()

    news = rows_to_news(rows)

    conn.close()

    return {
        "total": len(news),
        "news": news
    }
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

from fastapi import HTTPException

def news_by_source(source_name: str):


 conn = get_connection()
 cursor = conn.cursor()

 cursor.execute(
    "SELECT * FROM news WHERE source = ?",
    (source_name,)
)
 rows = cursor.fetchall()

 news = rows_to_news(rows)
 if not news:
        raise HTTPException(
            status_code=404,
            detail="No news found for this source."
        )

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
def update_news(title: str, source: str, published: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE news
        SET source = ?, published = ?
        WHERE title = ?
    """, (
        source,
        published,
        title
    ))

    conn.commit()
    conn.close()

    return {
        "message": "News updated successfully"
    }
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


def test():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM news")

    count = cursor.fetchone()[0]

    conn.close()

    return {
        "count": count
    }
def count_news():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM news
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return {
        "total_news": total
    }