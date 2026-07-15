from fastapi import APIRouter
import app.services.search_service as search_service
from app.schemas import SearchRequest

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.post("")
def search_news(item: SearchRequest):
    return search_service.search_news(
        item.keyword,
        item.source,
        item.date)