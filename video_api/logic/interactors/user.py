import datetime as dt
import uuid

from domain.entities.advert import Advert
from domain.entities.user import User
from infra.uow import UnitOfWork
from logic.use_cases.advert import CreateAdvertUseCase, FetchAdvertUseCase, FetchListAdvertUseCase
from logic.use_cases.user.auth_session import AuthUserUseCase
from logic.use_cases.user.create_user import CreateUserUseCase
from logic.use_cases.user.fetch_user import FetchUserUseCase
from logic.use_cases.user.login_user import LoginUserUseCase


class UserInteractor:
    def __init__(self, uow: UnitOfWork, session_ttl: dt.timedelta) -> None:
        self.uow = uow

        self.session_ttl = session_ttl

    async def authenticate(self, login: str, password: str) -> uuid.UUID:
        async with self.uow:
            user = await FetchUserUseCase(self.uow, login, password)()
            return await LoginUserUseCase(self.uow, user, password, self.session_ttl)()

    async def create(self, login: str, password: str) -> None:
        async with self.uow:
            return await CreateUserUseCase(self.uow, login, password)()

    async def auth_session(self, session_id: uuid.UUID) -> User | None:
        async with self.uow:
            return await AuthUserUseCase(self.uow, session_id)()
