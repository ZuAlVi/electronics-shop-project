import pytest

from src.phone import Phone


@pytest.fixture
def phone_fixture():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(phone_fixture):
    assert phone_fixture.name == 'iPhone 14'
    assert phone_fixture.price == 120000
    assert phone_fixture.quantity == 5
    assert phone_fixture.number_of_sim == 2


def test_phone_repr(phone_fixture):
    assert repr(phone_fixture) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_number_of_sim(phone_fixture):
    assert phone_fixture.number_of_sim == 2
    try:
        phone_fixture.number_of_sim = 0
    except ValueError:
        'Количество физических SIM-карт должно быть целым числом больше нуля.'
    phone_fixture.number_of_sim = 1
    assert phone_fixture.number_of_sim == 1


