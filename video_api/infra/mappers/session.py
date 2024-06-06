from domain.entities.session import Session
from infra.db.orm import SessionORM


class SessionORMMapper:
    @staticmethod
    def to_orm(session: Session) -> SessionORM:
        return SessionORM(
            user_id=session.user_id,
            expired_at=session.expired_at,
        )

    @staticmethod
    def from_orm(session: SessionORM) -> Session:
        return Session(
            id=session.id,
            expired_at=session.expired_at,
            user_id=session.user_id,
        )
