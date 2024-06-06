from dataclasses import dataclass

from domain.values.positive_int import PositiveInt

from .base import BaseEntity


@dataclass(frozen=True, eq=False, kw_only=True)
class Advert(BaseEntity):
    title: str
    ad_id: str
    author: str
    view_count: PositiveInt
    position: PositiveInt
