# ruff: noqa
import typing as tp
from dataclasses import dataclass

if tp.TYPE_CHECKING:
    from types import EllipsisType

T = tp.TypeVar("T")


@dataclass
class NotInitializedError(Exception):
    name: str
    class_: tp.Type

    @property
    def message(self) -> str:
        return f"Variable `{self.name}` from `{self.class_.__name__}` not initialized"

    def __str__(self) -> str:
        return self.message


class InitializeLaterVar(tp.Generic[T]):
    def __set_name__(self, _, name: str) -> None:
        self.name = name
        self.value: EllipsisType | T = ...

    def __get__(self, _, class_: tp.Type) -> T:
        if self.value is ...:
            raise NotInitializedError(self.name, class_)
        return self.value

    def __set__(self, _, value: T) -> None:
        self.value = value

    def __delete__(self, _) -> None:
        self.value = ...
