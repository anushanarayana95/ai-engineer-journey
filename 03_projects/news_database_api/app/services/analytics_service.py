from app.database import get_connection
def get_analytics():
    conn = get_connection()

    try:
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

        source_counts = dict(cursor.fetchall())

        return {
            "total_articles": total_articles,
            "sources": source_counts
        }

    finally:
        conn.close()