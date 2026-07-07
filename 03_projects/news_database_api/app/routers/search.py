from fastapi import APIRouter
from app.services import search_service

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.get("/{keyword}")
def search(keyword: str):
    return search_service.search_news(keyword)