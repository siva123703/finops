from fastapi import APIRouter
from app.config import settings

router = APIRouter()


@router.get("/")
def home():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
    }