import uuid

from domain.entities.advert import Advert
from infra.uow import UnitOfWork
from logic.use_cases.advert import CreateAdvertUseCase, FetchAdvertUseCase, FetchListAdvertUseCase


class AdvertInteractor:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def fetch(self, ad_id: uuid.UUID) -> Advert | None:
        async with self.uow:
            return await FetchAdvertUseCase(self.uow, ad_id)()

    async def fetch_list(self, limit: int, offset: int) -> list[Advert]:
        async with self.uow:
            return await FetchListAdvertUseCase(self.uow, limit, offset)()

    async def create(self, advert: Advert) -> uuid.UUID:
        async with self.uow:
            return await CreateAdvertUseCase(self.uow, advert)()
