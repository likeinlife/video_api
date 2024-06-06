import typing as tp
import uuid

from domain.entities.user import User


class IUserRepository(tp.Protocol):
    async def fetch(self, user_id: uuid.UUID) -> User | None: ...

    async def fetch_by_login(self, login: str) -> User | None: ...

    async def create(self, user: User) -> uuid.UUID: ...
