import pytest

from domain.values.login import EmptyUserLoginError, UserLogin
from domain.values.positive_int import InvalidPositiveIntError, PositiveInt


def test_positive_int() -> None:
    assert PositiveInt(10).as_generic_type() == 10


def test_negative_int() -> None:
    with pytest.raises(InvalidPositiveIntError):
        assert PositiveInt(-10)


def test_user_login() -> None:
    assert UserLogin("test").as_generic_type() == "test"


def test_empty_user_login() -> None:
    with pytest.raises(EmptyUserLoginError):
        assert UserLogin("")
