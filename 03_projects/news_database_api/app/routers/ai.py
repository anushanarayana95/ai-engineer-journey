from fastapi import APIRouter
from app.services import ai_service

router = APIRouter(
    tags=["AI"]
)

@router.get("/sync_news")
def sync():
    return ai_service.sync_news()

@router.post("/summarize-news/{title}")
def summarize(title: str):
   return ai_service.summarize_news(title)
@router.post("/analyze-news/{title}")
def analyze_news(title: str):
    return ai_service.analyze_news(title)
