from http import HTTPStatus
from uuid import UUID

import httpx

from .url_resolver import UrlResolver


def test_get_list(http_client: httpx.Client, session: str, url_resolver: UrlResolver):
    limit_offset = {"limit": 10, "offset": 0}

    response = http_client.get(url_resolver.advert_list(), cookies={"Authorization": session}, params=limit_offset)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 10


def test_get_detail(http_client: httpx.Client, session: str, url_resolver: UrlResolver):
    limit_offset = {"limit": 10, "offset": 0}

    lst_response = http_client.get(url_resolver.advert_list(), cookies={"Authorization": session}, params=limit_offset)
    assert lst_response.status_code == HTTPStatus.OK
    first_id = lst_response.json()[0]["id"]

    response = http_client.get(url_resolver.advert_detail(UUID(first_id)), cookies={"Authorization": session})
    assert response.status_code == HTTPStatus.OK
