from fastapi import APIRouter, status
import app.services.news_service as news_service
from fastapi import APIRouter, status, Query
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

@router.get("")
def get_news(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    source: str | None = None,
    sort_by: str = "published",
    order: str = "DESC"
):
    return news_service.get_all_news(
        page,
        limit,
        source,
        sort_by,
        order
    )
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

@router.get("/filter")
def filter_news(start_date: str, end_date: str):
    return news_service.filter_news(start_date, end_date)