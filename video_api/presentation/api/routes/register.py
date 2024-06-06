from fastapi import APIRouter, FastAPI

from . import advert, common, user


def register(app: FastAPI) -> None:  # noqa: ARG001
    """Register all routes."""
    router = APIRouter()
    common.register(router)
    user.register(router)
    advert.register(router)
