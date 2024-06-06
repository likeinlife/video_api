from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class AdvertORM(Base):
    __tablename__ = "advert"

    title: Mapped[str]
    author: Mapped[str]
    view_count: Mapped[int]
    position: Mapped[int]
