import logging
from fastapi import FastAPI
from app.api import status
from app.core.settings import settings
from app.database.session import global_init

log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(
        status.router,
        tags=["Status"],
        prefix=settings.API_V1_PREFIX
    )
    return application

app = create_application()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    global_init()