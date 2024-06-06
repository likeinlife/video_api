import datetime as dt
import uuid

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class AdvertORM(Base):
    __tablename__ = "advert"

    title: Mapped[str]
    author: Mapped[str]
    view_count: Mapped[int]
    position: Mapped[int]


class UserORM(Base):
    __tablename__ = "user"

    login: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hash_password: Mapped[str]


class SessionORM(Base):
    __tablename__ = "session"

    user_id: Mapped[uuid.UUID] = mapped_column(sa.ForeignKey("user.id"))
    user: Mapped[UserORM] = relationship("UserORM", init=False)
    expired_at: Mapped[dt.datetime]
