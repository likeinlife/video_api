import datetime as dt
import uuid
from dataclasses import dataclass

from .base import BaseEntity


@dataclass(frozen=True, eq=False, kw_only=True)
class Session(BaseEntity):
    expired_at: dt.datetime
    user_id: uuid.UUID
