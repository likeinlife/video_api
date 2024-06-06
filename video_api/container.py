import datetime as dt
from functools import lru_cache

from dishka import Container, Provider, Scope, make_container, provide
from sqlalchemy.ext import asyncio as sa_async

from core.settings import settings
from infra.db.base import create_async_engine, create_session_maker
from infra.uow import UnitOfWork
from logic.interactors.advert import AdvertInteractor
from logic.interactors.user import UserInteractor


class AppProvider(Provider):
    @provide(scope=Scope.APP)
    def _get_engine(self) -> sa_async.AsyncEngine:
        return create_async_engine(settings.db.get_url())

    @provide(scope=Scope.APP)
    def _get_session(self, engine: sa_async.AsyncEngine) -> sa_async.async_sessionmaker:
        return create_session_maker(engine)

    @provide(scope=Scope.APP)
    def _get_uow(self, session_maker: sa_async.async_sessionmaker) -> UnitOfWork:
        return UnitOfWork(session_maker)

    @provide(scope=Scope.APP)
    def _get_advert_interactor(self, uow: UnitOfWork) -> AdvertInteractor:
        return AdvertInteractor(uow)

    @provide(scope=Scope.APP)
    def _get_user_interactor(self, uow: UnitOfWork) -> UserInteractor:
        ttl = dt.timedelta(seconds=settings.session.ttl)
        return UserInteractor(uow, ttl)


@lru_cache(1)
def get_container() -> Container:
    return make_container(AppProvider())
