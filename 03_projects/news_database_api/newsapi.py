import requests
import sqlite3
import pandas as pd
API_KEY = "8b390caa5b8341729ba9e2b87e82b1c9"

url = (
    f"https://newsapi.org/v2/top-headlines?"
    f"country=us&apiKey={API_KEY}"
)

response = requests.get(url)

data = response.json()

articles = data["articles"]
print(len(articles))

conn = sqlite3.connect("news.db")

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    title TEXT,
    source TEXT,
    published TEXT
)
""")
for article in articles:
    cursor.execute("""
INSERT INTO news
VALUES (?, ?, ?)
""",
(
    article["title"],
    article["source"]["name"],
    article["publishedAt"]
))
    conn.commit()
    cursor.execute("""
SELECT COUNT(*)
FROM news
""")

count = cursor.fetchone()[0]


print("Total Articles:", count)