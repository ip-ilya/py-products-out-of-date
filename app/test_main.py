import pytest
from unittest.mock import Mock
from unittest import mock
from datetime import date

from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "datetime_return_value,result",
    [
        (
            date(2022, 2, 1),
            [],
        ),
        (
            date(2023, 1, 1),
            ["salmon", "chicken", "duck"],
        ),
        (
            date(2022, 2, 6),
            ["chicken", "duck"],
        ),
        (
            date(2022, 2, 4),
            ["duck"],
        )

    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mocked_datetime: Mock,
        products: list,
        datetime_return_value: date,
        result: list
) -> None:
    mocked_datetime.today.return_value = datetime_return_value
    assert outdated_products(products) == result
