import uuid
from dataclasses import dataclass

from domain.entities.advert import Advert
from infra.uow import UnitOfWork
from logic.use_cases.interface import IUseCase


@dataclass(frozen=True, eq=False)
class CreateAdvertUseCase(IUseCase[uuid.UUID]):
    uow: UnitOfWork
    advert: Advert

    async def __call__(self) -> uuid.UUID:
        return await self.uow.advert.create(self.advert)
