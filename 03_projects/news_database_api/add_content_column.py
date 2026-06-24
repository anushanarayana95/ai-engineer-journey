import sqlite3

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE news
ADD COLUMN content TEXT
""")

conn.commit()
conn.close()

print("Content column added")