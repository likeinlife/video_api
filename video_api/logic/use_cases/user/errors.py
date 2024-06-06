from dataclasses import dataclass

from domain.errors import BaseError


class UserUseCaseError(BaseError):
    @property
    def message(self) -> str:
        return "User use case error"


@dataclass(frozen=True, eq=False)
class UserNotFoundError(UserUseCaseError):
    login: str

    @property
    def message(self) -> str:
        return f"User not found: {self.login}"


@dataclass(frozen=True, eq=False)
class WrongPasswordError(UserUseCaseError):
    login: str

    @property
    def message(self) -> str:
        return f"Wrong password error on user: {self.login}"
