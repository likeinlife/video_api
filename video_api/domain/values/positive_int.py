from dataclasses import dataclass

from domain.errors import BaseError

from .base import BaseValueObject


@dataclass(frozen=True, eq=False)
class InvalidPositiveIntError(BaseError):
    value: int

    @property
    def message(self) -> str:
        return f"{self.value} is not a positive integer"


class PositiveInt(BaseValueObject[int]):
    def validate(self) -> None:
        if self.value < 0:
            raise InvalidPositiveIntError(self.value)

    def as_generic_type(self) -> int:
        return self.value
