def rows_to_news(rows):
    news = []

    for row in rows:
        news.append({
            "title": row["title"],
            "source": row["source"],
            "published": row["published"]
        })

    return news