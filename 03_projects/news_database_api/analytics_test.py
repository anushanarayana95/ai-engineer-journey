import sqlite3

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("""
SELECT source, COUNT(*)
FROM news
GROUP BY source
ORDER BY COUNT(*) DESC
""")

for row in cursor.fetchall():
    print(row)

conn.close()