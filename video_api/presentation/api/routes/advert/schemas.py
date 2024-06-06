from pydantic import BaseModel

from domain.entities.advert import Advert


class AdvertSchema(BaseModel):
    title: str
    author: str
    view_count: int
    position: int

    @classmethod
    def from_domain(cls, advert: Advert) -> "AdvertSchema":
        return cls(
            title=advert.title,
            author=advert.author,
            view_count=advert.view_count.as_generic_type(),
            position=advert.position.as_generic_type(),
        )
