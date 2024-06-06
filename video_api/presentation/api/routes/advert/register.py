from fastapi import APIRouter

from . import endpoints


def register(router: APIRouter) -> None:
    _router = APIRouter(tags=["advert"])
    _router.include_router(endpoints.router)

    router.include_router(_router)
