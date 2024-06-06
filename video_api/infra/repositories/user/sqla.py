import uuid

import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.user import User
from domain.protocols.user import IUserRepository
from infra.db.orm import UserORM
from infra.mappers.user import UserORMMapper
from infra.repositories.errors import UserLoginAlreadyExistsError


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def fetch(self, user_id: uuid.UUID) -> User | None:
        query = sa.select(UserORM).where(UserORM.id == user_id)
        result = (await self.session.execute(query)).scalar_one_or_none()
        if result is None:
            return None
        return UserORMMapper.from_orm(result)

    async def fetch_by_login(self, login: str) -> User | None:
        query = sa.select(UserORM).where(UserORM.login == login)
        result = (await self.session.execute(query)).scalar_one_or_none()
        if result is None:
            return None
        return UserORMMapper.from_orm(result)

    async def create(self, user: User) -> uuid.UUID:
        orm = UserORMMapper.to_orm(user)
        self.session.add(orm)
        try:
            await self.session.flush()
            await self.session.refresh(orm)
        except IntegrityError as e:
            raise UserLoginAlreadyExistsError(user.login.as_generic_type()) from e
        else:
            return orm.id
