import datetime as dt
import uuid
from dataclasses import dataclass
from hashlib import sha512

from domain.entities.session import Session
from domain.entities.user import User
from infra.uow import UnitOfWork
from logic.use_cases.interface import IUseCase

from .errors import WrongPasswordError


@dataclass(frozen=True, eq=False)
class AuthUserUseCase(IUseCase):
    uow: UnitOfWork
    session_id: uuid.UUID

    async def __call__(self) -> None | User:
        return await self.uow.session.fetch(self.session_id)
