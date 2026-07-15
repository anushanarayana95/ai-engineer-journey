from app.database import get_connection
from app.utils.helpers import rows_to_news
from fastapi import HTTPException
def get_all_news(
    page=1,
    limit=10,
    source=None,
    sort_by="published",
    order="DESC"
):

    conn = get_connection()
    cursor = conn.cursor()

    # calculate offset
    offset = (page - 1) * limit


    # safety validation
    allowed_sort = [
        "published",
        "title",
        "source"
    ]

    if sort_by not in allowed_sort:
        sort_by = "published"


    if order not in ["ASC", "DESC"]:
        order = "DESC"


    # base query
    query = "SELECT * FROM news WHERE 1=1"

    params = []


    # filter by source
    if source:
        query += " AND source = ?"
        params.append(source)


    # sorting
    query += f" ORDER BY {sort_by} {order}"


    # pagination
    query += " LIMIT ? OFFSET ?"

    params.extend([
        limit,
        offset
    ])


    cursor.execute(query, params)

    rows = cursor.fetchall()


    news = rows_to_news(rows)


    # total count query
    count_query = "SELECT COUNT(*) FROM news WHERE 1=1"
    count_params = []


    if source:
        count_query += " AND source = ?"
        count_params.append(source)


    cursor.execute(
        count_query,
        count_params
    )


    total = cursor.fetchone()[0]
    total_pages = (total + limit - 1) // limit
    has_next = page < total_pages
    has_previous = page > 1



    conn.close()

    return {
         "page": page,
    "limit": limit,
    "total": total,
    "total_pages": total_pages,
    "has_next": has_next,
    "has_previous": has_previous,
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
def filter_news(start_date: str, end_date: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM news
        WHERE published BETWEEN ? AND ?
        ORDER BY published DESC
    """, (start_date, end_date))

    rows = cursor.fetchall()

    conn.close()

    news = rows_to_news(rows)

    return {
        "total": len(news),
        "news": news
    }