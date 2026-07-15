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
        from app.database import get_connection

def source_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT source,
               COUNT(*) AS count
        FROM news
        GROUP BY source
        ORDER BY count DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows
def daily_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            substr(published,1,10) AS date,
            COUNT(*) AS count
        FROM news
        GROUP BY date
        ORDER BY date DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    result = []

    for row in rows:
        result.append({
            "date": row["date"],
            "count": row["count"]
        })

    return result

def top_sources(limit=5):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            source,
            COUNT(*) AS count
        FROM news
        GROUP BY source
        ORDER BY count DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    result = []

    for row in rows:
        result.append({
            "source": row["source"],
            "count": row["count"]
        })

    return result