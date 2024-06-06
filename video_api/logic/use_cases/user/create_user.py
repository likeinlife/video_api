from dataclasses import dataclass
from hashlib import sha512

from domain.entities.user import User
from domain.values.login import UserLogin
from infra.uow import UnitOfWork
from logic.use_cases.interface import IUseCase


@dataclass(frozen=True, eq=False)
class CreateUserUseCase(IUseCase):
    uow: UnitOfWork
    login: str
    init_password: str

    async def __call__(self) -> None:
        hashed_password = sha512(self.init_password.encode()).hexdigest()

        user = User(
            login=UserLogin(self.login),
            hash_password=hashed_password,
        )

        await self.uow.user.create(user)
