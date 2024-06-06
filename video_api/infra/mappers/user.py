from domain.entities.user import User
from domain.values.login import UserLogin
from infra.db.orm import UserORM


class UserORMMapper:
    @staticmethod
    def to_orm(user: User) -> UserORM:
        return UserORM(
            hash_password=user.hash_password,
            login=user.login.as_generic_type(),
        )

    @staticmethod
    def from_orm(user: UserORM) -> User:
        return User(
            id=user.id,
            hash_password=user.hash_password,
            login=UserLogin(user.login),
        )
