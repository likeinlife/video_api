from dataclasses import dataclass

from domain.errors import BaseError


class RepositoryError(BaseError):
    @property
    def message(self) -> str:
        return "Repository error message"


@dataclass(frozen=True, eq=False)
class UserLoginAlreadyExistsError(BaseError):
    login: str

    @property
    def message(self) -> str:
        return f"User login already exists: {self.login}"
