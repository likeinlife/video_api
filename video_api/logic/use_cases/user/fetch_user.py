from dataclasses import dataclass

from domain.entities.user import User
from infra.uow import UnitOfWork
from logic.use_cases.interface import IUseCase

from .errors import UserNotFoundError


@dataclass(frozen=True, eq=False)
class FetchUserUseCase(IUseCase):
    uow: UnitOfWork
    login: str
    init_password: str

    async def __call__(self) -> User:
        result = await self.uow.user.fetch_by_login(self.login)

        if not result:
            raise UserNotFoundError(login=self.login)

        return result
