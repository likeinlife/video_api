from dataclasses import dataclass

from domain.errors import BaseError

from .base import BaseValueObject


class EmptyUserLoginError(BaseError):
    @property
    def message(self) -> str:
        return "User login must not be empty"


class UserLogin(BaseValueObject[str]):
    def validate(self) -> None:
        if not self.value:
            raise EmptyUserLoginError

    def as_generic_type(self) -> str:
        return self.value
