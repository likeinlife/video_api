import typing as tp
from uuid import UUID

from dishka import Container
from fastapi import Depends, HTTPException, Request

from container import get_container
from domain.entities.user import User
from logic.interactors.user import UserInteractor


async def user_getter_dependency(
    request: Request,
    container: tp.Annotated[Container, Depends(get_container)],
) -> User:
    session_token = request.headers.get("Authorization")
    if not session_token:
        raise HTTPException(status_code=403, detail="No session token provided")

    session_token = session_token.lstrip("Bearer ")  # noqa: B005
    try:
        session_uuid = UUID(session_token)
    except ValueError as e:
        raise HTTPException(status_code=403, detail="Invalid session token") from e

    interactor = container.get(UserInteractor)

    user = await interactor.auth_session(session_uuid)

    if not user:
        raise HTTPException(status_code=403, detail="Invalid session token")
    return user
