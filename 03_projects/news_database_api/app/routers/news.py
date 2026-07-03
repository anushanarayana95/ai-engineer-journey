from fastapi import APIRouter

from app.schemas import NewsItem
from app.services.news_service import get_all_news
from app.services.news_service import add_news

router = APIRouter(
    prefix="/news",
    tags=["News"]
)


@router.get("")
def get_news():
    return get_all_news()

# -----------------------------

@router.get("/count")
def count_news():
    return count_news()


@router.get("/latest")
def latest_news():
    return latest_news()


@router.get("/source/{source_name}")
def news_by_source(source_name: str):
    return news_by_source(source_name)

@router.post("")
def create_news(item: NewsItem):

    return add_news(
        item.title,
        item.source,
        item.published
    
    )