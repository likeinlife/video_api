from http import HTTPStatus

import httpx

from ._types import UserGeneratorType
from .url_resolver import UrlResolver


def test_no_session_advert_list(
    http_client: httpx.Client,
    url_resolver: UrlResolver,
) -> None:
    response = http_client.get(url_resolver.advert_list())
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_wrong_session(
    http_client: httpx.Client,
    url_resolver: UrlResolver,
) -> None:
    cookies = {"Authorization": "Bearer 123"}
    response = http_client.get(url_resolver.advert_list(), cookies=cookies)
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_user_register(
    http_client: httpx.Client,
    url_resolver: UrlResolver,
    user_generator: UserGeneratorType,
) -> None:
    user_creds = user_generator()
    body = {"login": user_creds.login, "password": user_creds.password}
    response = http_client.post(url_resolver.user_register(), json=body)
    assert response.status_code == HTTPStatus.CREATED


def test_user_already_exists(
    http_client: httpx.Client,
    url_resolver: UrlResolver,
    user_generator: UserGeneratorType,
) -> None:
    user_creds = user_generator()
    body = {"login": user_creds.login, "password": user_creds.password}
    http_client.post(url_resolver.user_register(), json=body)
    response = http_client.post(url_resolver.user_register(), json=body)

    assert response.status_code == HTTPStatus.CONFLICT


def test_user_login(
    http_client: httpx.Client,
    url_resolver: UrlResolver,
    user_generator: UserGeneratorType,
) -> None:
    user_creds = user_generator()
    user_json = {"login": user_creds.login, "password": user_creds.password}

    http_client.post(url_resolver.user_register(), json=user_json)

    response = http_client.post(url_resolver.user_login(), json=user_json)
    session_token = response.cookies.get("Authorization")

    assert session_token is not None, response.json()

    assert response.status_code == HTTPStatus.OK
