from fastapi import APIRouter
from app.core.settings import settings

router = APIRouter(tags=["Status"])

@router.get("/status")
async def ping():
    return {
        "success": True,
        "version": settings.APP_VERSION
    }