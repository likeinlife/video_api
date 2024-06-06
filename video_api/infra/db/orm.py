from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class AdvertORM(Base):
    title: Mapped[str]
    ad_id: Mapped[str] = mapped_column(primary_key=True, index=True)
    author: Mapped[str]
    view_count: Mapped[int]
    position: Mapped[int]
