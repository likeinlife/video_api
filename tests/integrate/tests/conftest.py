import random
from http import HTTPStatus
from string import ascii_lowercase

import httpx
import pytest

from ._types import UserCredentials, UserGeneratorType
from .url_resolver import UrlResolver


@pytest.fixture(scope="session")
def http_client() -> httpx.Client:
    return httpx.Client()


@pytest.fixture(scope="session")
def user_generator() -> UserGeneratorType:
    def generator(x: int):
        return "".join([random.choice(ascii_lowercase) for _ in range(x)])

    def user_fabric() -> UserCredentials:
        return UserCredentials(login=generator(10), password=generator(10))

    return user_fabric


@pytest.fixture(scope="session")
def url_resolver() -> UrlResolver:
    return UrlResolver()


@pytest.fixture(scope="session")
def session(
    user_generator: UserGeneratorType,
    http_client: httpx.Client,
    url_resolver: UrlResolver,
) -> str:
    user_creds = user_generator()
    user_dict = {"login": user_creds.login, "password": user_creds.password}

    register_response = http_client.post(url_resolver.user_register(), json=user_dict)
    assert register_response.status_code == HTTPStatus.CREATED, register_response.content

    response = http_client.post(url_resolver.user_login(), json=user_dict)
    session = response.cookies.get("Authorization")

    assert response.status_code == HTTPStatus.OK, response.content
    if not session:
        raise RuntimeError("No session token")  # noqa: TRY003, EM101
    return session
