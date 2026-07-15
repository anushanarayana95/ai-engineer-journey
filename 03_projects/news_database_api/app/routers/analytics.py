from fastapi import APIRouter
import app.services.analytics_service as analytics_service

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/source-count")
def source_count():
    return analytics_service.source_count()
@router.get("/daily-count")
def daily_count():
    return analytics_service.daily_count()

@router.get("/top-sources")
def top_sources(limit: int = 5):
    return analytics_service.top_sources(limit)