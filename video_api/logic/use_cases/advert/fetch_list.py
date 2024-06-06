import uuid
from dataclasses import dataclass

from domain.entities.advert import Advert
from infra.uow import UnitOfWork
from logic.use_cases.interface import IUseCase


@dataclass(frozen=True, eq=False)
class FetchListAdvertUseCase(IUseCase[uuid.UUID]):
    uow: UnitOfWork
    offset: int
    limit: int

    async def __call__(self) -> list[Advert]:
        return await self.uow.advert.fetch_list(limit=self.limit, offset=self.offset)
