from fastapi import APIRouter, FastAPI

from . import common


def register(app: FastAPI) -> None:  # noqa: ARG001
    """Register all routes."""
    router = APIRouter()
    common.register(router)
