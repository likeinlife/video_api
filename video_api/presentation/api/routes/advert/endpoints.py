import typing as tp
import uuid

from dishka import Container
from fastapi import APIRouter, Depends, HTTPException, Path, Query

from container import get_container
from logic.interactors.advert import AdvertInteractor

from .schemas import AdvertSchema

router = APIRouter()


@router.get("/")
async def fetch_advert_list(
    container: tp.Annotated[Container, Depends(get_container)],
    limit: tp.Annotated[int, Query(gt=0, le=100)] = 10,
    offset: tp.Annotated[int, Query(gt=0)] = 0,
) -> list[AdvertSchema]:
    interactor = container.get(AdvertInteractor)
    result = await interactor.fetch_list(limit, offset)
    return [AdvertSchema.from_domain(advert) for advert in result]


@router.get("/{advert_id}/")
async def fetch_advert(
    container: tp.Annotated[Container, Depends(get_container)],
    advert_id: tp.Annotated[uuid.UUID, Path()],
) -> AdvertSchema:
    interactor = container.get(AdvertInteractor)
    result = await interactor.fetch(advert_id)
    if not result:
        raise HTTPException(status_code=404, detail="Advert not found")
    return AdvertSchema.from_domain(result)
