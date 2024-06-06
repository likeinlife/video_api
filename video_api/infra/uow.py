from types import TracebackType

from sqlalchemy.ext import asyncio as sa_async
from utils.init_later_var import InitializeLaterVar

from domain.protocols.advert import IAdvertRepository
from domain.protocols.session import ISessionRepository
from domain.protocols.user import IUserRepository
from infra.repositories.advert.sqla import AdvertRepository
from infra.repositories.session.sqla import SessionRepository
from infra.repositories.user.sqla import UserRepository


class UnitOfWork:
    advert = InitializeLaterVar[IAdvertRepository]()
    user = InitializeLaterVar[IUserRepository]()
    session = InitializeLaterVar[ISessionRepository]()

    def __init__(self, session_maker: sa_async.async_sessionmaker[sa_async.AsyncSession]) -> None:
        self.session_maker = session_maker

    async def __aenter__(self) -> None:
        self._session = self.session_maker()
        self.advert = AdvertRepository(self._session)
        self.user = UserRepository(self._session)
        self.session = SessionRepository(self._session)

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()
        await self._session.close()
        del self.advert

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
