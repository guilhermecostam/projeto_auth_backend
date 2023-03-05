from app.api.routes import users, status
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(status.router)
api_router.include_router(users.router)