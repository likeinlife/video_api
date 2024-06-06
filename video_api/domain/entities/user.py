from dataclasses import dataclass

from domain.values.login import UserLogin

from .base import BaseEntity


@dataclass(frozen=True, eq=False, kw_only=True)
class User(BaseEntity):
    login: UserLogin
    hash_password: str
