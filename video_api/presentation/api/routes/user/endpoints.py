import typing as tp

from asyncpg import InvalidPasswordError
from dishka import Container
from fastapi import APIRouter, Depends, HTTPException, Response

from container import get_container
from core.settings import settings
from infra.repositories.errors import UserLoginAlreadyExistsError
from logic.interactors.user import UserInteractor
from logic.use_cases.user.errors import UserNotFoundError

from .schemas import UserLoginSchema, UserRegisterSchema

router = APIRouter()


@router.post("/register/")
async def register(
    container: tp.Annotated[Container, Depends(get_container)],
    user: UserRegisterSchema,
) -> Response:
    interactor = container.get(UserInteractor)
    try:
        await interactor.create(user.login, user.password)
    except UserLoginAlreadyExistsError as e:
        raise HTTPException(status_code=409, detail="User already exists") from e
    return Response(status_code=201)


@router.post("/login/")
async def fetch_advert(
    container: tp.Annotated[Container, Depends(get_container)],
    user: UserLoginSchema,
) -> Response:
    response = Response(status_code=200)
    interactor = container.get(UserInteractor)
    try:
        result = await interactor.authenticate(user.login, user.password)
    except (InvalidPasswordError, UserNotFoundError) as e:
        raise HTTPException(status_code=403, detail="Wrong password or login") from e

    response.set_cookie("Authorization", f"Bearer {result}", httponly=True, secure=True, expires=settings.session.ttl)
    return response
