import uuid
from dataclasses import dataclass

from domain.entities.user import User
from infra.uow import UnitOfWork
from logic.use_cases.interface import IUseCase


@dataclass(frozen=True, eq=False)
class AuthUserUseCase(IUseCase):
    uow: UnitOfWork
    session_id: uuid.UUID

    async def __call__(self) -> None | User:
        return await self.uow.session.fetch(self.session_id)
