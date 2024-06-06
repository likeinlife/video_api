import uuid

from pydantic import BaseModel

from domain.entities.advert import Advert


class AdvertSchema(BaseModel):
    id: uuid.UUID
    title: str
    author: str
    view_count: int
    position: int

    @classmethod
    def from_domain(cls, advert: Advert) -> "AdvertSchema":
        return cls(
            id=advert.id,
            title=advert.title,
            author=advert.author,
            view_count=advert.view_count.as_generic_type(),
            position=advert.position.as_generic_type(),
        )
