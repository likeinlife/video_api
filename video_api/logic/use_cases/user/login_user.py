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
class LoginUserUseCase(IUseCase):
    uow: UnitOfWork
    user: User
    password: str
    session_ttl: dt.timedelta

    async def __call__(self) -> uuid.UUID:
        hashed_password = sha512(self.password.encode()).hexdigest()

        if hashed_password != self.user.hash_password:
            raise WrongPasswordError(login=self.user.login.as_generic_type())

        session_expire_at = dt.datetime.now(tz=None) + self.session_ttl  # noqa: DTZ005
        return await self.uow.session.create(Session(user_id=self.user.id, expired_at=session_expire_at))
