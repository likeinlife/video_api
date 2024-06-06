import typing as tp
import uuid

from domain.entities.advert import Advert


class IAdvertRepository(tp.Protocol):
    async def fetch(self, ad_id: str) -> Advert | None: ...

    async def fetch_list(self, limit: int, offset: int) -> list[Advert]: ...

    async def create(self, advert: Advert) -> uuid.UUID: ...
