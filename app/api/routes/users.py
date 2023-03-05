from fastapi import APIRouter

router = APIRouter(tags=["Users"])

@router.get("/users")
async def users():
    return {
        "success": True
    }