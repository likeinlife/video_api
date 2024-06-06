import uuid

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.advert import Advert
from domain.protocols.advert import IAdvertRepository
from infra.db.orm import AdvertORM
from infra.mappers.advert import AdvertORMMapper


class AdvertRepository(IAdvertRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def fetch(self, ad_id: str) -> Advert | None:
        query = sa.select(AdvertORM).where(AdvertORM.ad_id == ad_id)
        result = (await self.session.execute(query)).scalar_one_or_none()
        if result is None:
            return None
        return AdvertORMMapper.from_orm(result)

    async def fetch_list(self, limit: int, offset: int) -> list[Advert]:
        query = sa.select(AdvertORM).limit(limit).offset(offset)
        result = (await self.session.execute(query)).scalars().all()
        return [AdvertORMMapper.from_orm(res) for res in result]

    async def create(self, advert: Advert) -> uuid.UUID:
        orm = AdvertORMMapper.to_orm(advert)
        self.session.add(orm)
        await self.session.flush()
        await self.session.refresh(orm)
        return orm.id
