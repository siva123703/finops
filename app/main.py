from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.routes import router as root_router
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(root_router)
app.include_router(health_router)