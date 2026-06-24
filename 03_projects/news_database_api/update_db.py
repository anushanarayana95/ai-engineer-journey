import sqlite3

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("ALTER TABLE news ADD COLUMN summary TEXT")
cursor.execute("ALTER TABLE news ADD COLUMN category TEXT")
cursor.execute("ALTER TABLE news ADD COLUMN keywords TEXT")

conn.commit()
conn.close()

print("Columns added successfully")