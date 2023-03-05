from fastapi import APIRouter, Depends
from app.core.settings import settings

router = APIRouter()

@router.get("/status")
async def ping():
    return {
        "success": True,
        "version": settings.APP_VERSION
    }