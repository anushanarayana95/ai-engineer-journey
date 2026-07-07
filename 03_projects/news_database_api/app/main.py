import sqlite3
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os
from app.routers.news import router as news_router
from google.genai.errors import ServerError
from app.routers.analytics import router as analytics_router
app = FastAPI()
app.include_router(news_router)
app.include_router(analytics_router)
from app.routers.search import router as search_router
app.include_router(search_router)
from app.routers.ai import router as ai_router

app.include_router(ai_router)


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

from app.database import get_connection

# -----------------------------
from app.schemas import NewsItem


# Home Endpoint

# -----------------------------

@app.get("/")
def home():
 return {
"message": "News API is running",
"version": "1.0"
}

# -----------------------------


# -----------------------------

@app.delete("/news/fake/string")
def delete_fake_news():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM news WHERE title = 'string'"
    )

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return {
        "deleted": deleted
    }





