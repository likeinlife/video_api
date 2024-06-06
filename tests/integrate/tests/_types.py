from dataclasses import dataclass
from typing import Callable, TypeAlias


@dataclass
class UserCredentials:
    login: str
    password: str


UserGeneratorType: TypeAlias = Callable[[], UserCredentials]
