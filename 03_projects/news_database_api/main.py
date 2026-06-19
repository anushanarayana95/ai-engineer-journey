
import sqlite3

conn = sqlite3.connect("03_projects/news_database_api/news.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    title TEXT,
    source TEXT,
    published TEXT
)
""")

cursor.execute("""
INSERT INTO news
VALUES (
    'AI News',
    'BBC',
    '2026-06-16'
)
""")



print("News Inserted Successfully")





cursor.execute("""
SELECT COUNT(*)
FROM news
""")
rows = cursor.fetchall()

print(rows)
print(rows[0])


conn.commit()



conn.close()