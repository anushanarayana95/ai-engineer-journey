from app.database import get_connection

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

    return [dict(row) for row in results]