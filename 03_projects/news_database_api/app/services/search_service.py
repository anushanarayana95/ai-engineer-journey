from app.database import get_connection
from app.utils.helpers import rows_to_news

def search_news(keyword=None, source=None, date=None):

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM news WHERE 1=1"
    params = []

    if keyword:
        query += " AND title LIKE ?"
        params.append(f"%{keyword}%")

    if source:
        query += " AND source = ?"
        params.append(source)

    if date:
        query += " AND published = ?"
        params.append(date)

    cursor.execute(query, params)

    rows = cursor.fetchall()

    conn.close()

    news = rows_to_news(rows)

    return {
        "total": len(news),
        "news": news
    }