import uuid
from dataclasses import dataclass

from domain.entities.advert import Advert
from infra.uow import UnitOfWork
from logic.use_cases.interface import IUseCase


@dataclass(frozen=True, eq=False)
class FetchAdvertUseCase(IUseCase[uuid.UUID]):
    uow: UnitOfWork
    advert_id: str

    async def __call__(self) -> Advert | None:
        return await self.uow.advert.fetch(self.advert_id)
