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
