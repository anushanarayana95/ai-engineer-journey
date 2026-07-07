from fastapi import APIRouter
from app.services import analytics_service
router = APIRouter(
    prefix="/Analytics",
    tags=["Analytics"]
)



@router.get("")
def analytics():
    return analytics_service.get_analytics()
