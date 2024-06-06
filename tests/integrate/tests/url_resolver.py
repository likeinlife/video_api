import typing as tp
import uuid


class ENDPOINTS:
    user_register = "/user/register/"
    user_login = "/user/login/"
    advert_list = "/advert/"
    advert_detail = "/advert/"


class UrlResolver:
    base_url: tp.Final = "http://app:8000"

    @classmethod
    def user_register(cls) -> str:
        return cls.base_url + ENDPOINTS.user_register

    @classmethod
    def user_login(cls) -> str:
        return cls.base_url + ENDPOINTS.user_login

    @classmethod
    def advert_list(cls) -> str:
        return cls.base_url + ENDPOINTS.advert_list

    @classmethod
    def advert_detail(cls, advert_id: uuid.UUID) -> str:
        return cls.base_url + ENDPOINTS.advert_detail + str(advert_id) + "/"
