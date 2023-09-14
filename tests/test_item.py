"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_fixture():
    return Item('Смартфон Samsung', 40000, 2)


def test_item_init(item_fixture):
    assert item_fixture.name == 'Смартфон Samsung'
    assert item_fixture.price == 40000
    assert item_fixture.quantity == 2
    assert len(Item.all) == 1


def test_item_calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 80000


def test_item_apply_discount(item_fixture):
    item_fixture.apply_discount()
    assert item_fixture.price == 32000


def test_item_name(item_fixture):
    item_fixture.name = 'Телевизор Sony'
    assert item_fixture.name == 'Телевизор '
    item_fixture.name = 'Sony'
    assert item_fixture.name == 'Sony'


def test_item_string_to_number():
    assert Item.string_to_number('93') == 93
    assert Item.string_to_number('567.015') == 567
    assert Item.string_to_number('time.015') is None
    assert Item.string_to_number('time') is None
