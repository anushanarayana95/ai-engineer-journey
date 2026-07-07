from app.database import get_connection
import os
import requests
from google import genai
from dotenv import load_dotenv
import os
from google.genai.errors import ServerError
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def sync_news():


 url = (
    f"https://newsapi.org/v2/top-headlines"
    f"?country=us&apiKey={NEWS_API_KEY}"
)
 response = requests.get(url)
 data = response.json()

 if data.get("status") != "ok":
    return {
        "error": data.get("message"),
        "code": data.get("code")
    }

 articles = data["articles"]
 

 conn = get_connection()
 cursor = conn.cursor()

 inserted = 0
 skipped = 0

 for article in articles:

    title = article["title"]

    cursor.execute(
        "SELECT COUNT(*) AS total FROM news WHERE title = ?",
        (title,)
    )

    exists = cursor.fetchone()["total"]
    
    if exists == 0:
     print("TITLE:", article.get("title"))
     print("DESCRIPTION:", article.get("description"))
     print("CONTENT:", article.get("content"))
     print("=" * 50)
     cursor.execute("""
INSERT INTO news
(title, source, published, content)
VALUES (?, ?, ?, ?)
""", (
    article["title"],
    article["source"]["name"],
    article["publishedAt"],
    article.get("content") or article.get("description") or ""
))

    inserted += 1

 else:
       skipped += 1
        

 conn.commit()
 conn.close()

 return {
    "message": "Sync completed",
    "inserted": inserted,
    "skipped": skipped
}

def summarize_news(title: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM news WHERE title = ?",
        (title,)
    )

    article = cursor.fetchone()

    if not article:
        conn.close()
        return {"error": "Article not found"}
        print("CONTENT:")
        print(article["content"])
    prompt = f"""
Summarize this news article in 3-5 sentences.

Title:
{article['title']}

Source:
{article['source']}

Content:
{article['content']}

"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    summary = response.text
    cursor.execute("""
        UPDATE news
        SET summary = ?
        WHERE title = ?
    """, (
        summary,
        title
    ))

    conn.commit()
    conn.close()

    return {
        "title": title,
        "summary": summary
    }

def analyze_news(title: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM news WHERE title = ?",
        (title,)
    )

    article = cursor.fetchone()

    if not article:
        conn.close()
        return {"error": "Article not found"}

    content = article["content"]

    prompt_text = f"""
Analyze the following news article.

Title:
{article['title']}

Content:
{content}

Return exactly in this format:

SUMMARY:
<2-3 sentence summary>

CATEGORY:
<one category>

KEYWORDS:
<comma separated keywords>
"""
    

    try:
    
     response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_text
    )
    except ServerError:
     return {
        "error": "Gemini API is temporarily busy. Please try again in a few minutes."
    }

    result = response.text

    print(result)

    summary = result.split("CATEGORY:")[0]
    summary = summary.replace("SUMMARY:", "").strip()

    category = result.split("CATEGORY:")[1]
    category = category.split("KEYWORDS:")[0].strip()

    keywords = result.split("KEYWORDS:")[1].strip()

    cursor.execute("""
        UPDATE news
        SET summary = ?,
            category = ?,
            keywords = ?
        WHERE title = ?
    """, (
        summary,
        category,
        keywords,
        title
    ))

    conn.commit()
    conn.close()

    return {
        "title": title,
        "summary": summary,
        "category": category,
        "keywords": keywords
    }