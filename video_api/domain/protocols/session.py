import datetime as dt
import typing as tp
import uuid

from domain.entities.session import Session
from domain.entities.user import User


class ISessionRepository(tp.Protocol):
    async def fetch(self, session_id: uuid.UUID) -> User | None: ...

    async def create(self, session: Session) -> uuid.UUID: ...
