from app.api.routes import auth, users, status
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(status.router)
api_router.include_router(users.router)
api_router.include_router(auth.router)