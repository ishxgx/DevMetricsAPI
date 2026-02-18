from fastapi import FastAPI
from app.core.config import settings
from app.routers import health, metrics

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)

app.include_router(health.router)
app.include_router(metrics.router)
