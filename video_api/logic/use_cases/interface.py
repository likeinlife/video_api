import abc
import typing as tp
from dataclasses import dataclass

R = tp.TypeVar("R")


@dataclass(frozen=True, eq=False)
class IUseCase(tp.Generic[R], abc.ABC):
    @abc.abstractmethod
    async def __call__(self) -> R:
        """Run use-case."""
