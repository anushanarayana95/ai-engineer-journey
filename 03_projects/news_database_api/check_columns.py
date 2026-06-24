import sqlite3

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(news)")

for row in cursor.fetchall():
    print(row)

conn.close()