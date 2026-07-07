from fastapi import APIRouter, status
import app.services.news_service as news_service

from app.schemas import (
    NewsItem,
    NewsResponse,
    MessageResponse
)

router = APIRouter(
    prefix="/news",
    tags=["News"]
)

# -----------------------------
# Get All News
# -----------------------------

@router.get("", response_model=NewsResponse)
def get_news():
    return news_service.get_all_news()

# -----------------------------
# Count News
# -----------------------------

@router.get("/count")
def count_news():
    return news_service.count_news()

# -----------------------------
# Latest News
# -----------------------------

@router.get("/latest")
def latest_news():
    return news_service.latest_news()

# -----------------------------
# Filter by Source
# -----------------------------

@router.get("/source/{source_name}")
def news_by_source(source_name: str):
    return news_service.news_by_source(source_name)

# -----------------------------
# Add News
# -----------------------------

@router.post(
    "",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED
)
def create_news(item: NewsItem):
    return news_service.add_news(
        item.title,
        item.source,
        item.published
    )

# -----------------------------
# Update News
# -----------------------------

@router.put("/{title}", response_model=MessageResponse)
def edit_news(title: str, item: NewsItem):
    return news_service.update_news(
        title,
        item.source,
        item.published
    )

# -----------------------------
# Delete News
# -----------------------------

@router.delete("/{title}", response_model=MessageResponse)
def remove_news(title: str):
    return news_service.delete_news(title)

# -----------------------------
# Test Route
# -----------------------------

@router.get("/test")
def test_news():
    return news_service.test()