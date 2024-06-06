from fastapi import APIRouter, FastAPI

from . import advert, common, user


def register(app: FastAPI) -> None:
    """Register all routes."""
    router = APIRouter()
    common.register(router)
    user.register(router)
    advert.register(router)

    app.include_router(router)
