import datetime as dt
import uuid

import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from domain.entities.session import Session
from domain.entities.user import User
from domain.protocols.session import ISessionRepository
from infra.db.orm import SessionORM
from infra.mappers.session import SessionORMMapper
from infra.mappers.user import UserORMMapper


class SessionRepository(ISessionRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, session: Session) -> uuid.UUID:
        orm = SessionORMMapper.to_orm(session)
        self.session.add(orm)
        await self.session.flush()
        await self.session.refresh(orm)
        return orm.id

    async def fetch(self, session_id: uuid.UUID) -> User | None:
        query = (
            sa.select(SessionORM)
            .where(SessionORM.id == session_id)
            .where(SessionORM.expired_at > sa.func.now())
            .options(joinedload(SessionORM.user))
        )
        result = (await self.session.execute(query)).scalar_one_or_none()
        if result is None:
            return None
        return UserORMMapper.from_orm(result.user)
