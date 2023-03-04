import os
from fastapi import APIRouter, Depends

router = APIRouter()
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

@router.get("/status")
async def ping():
    return {
        "success": True,
        "version": APP_VERSION,
    }