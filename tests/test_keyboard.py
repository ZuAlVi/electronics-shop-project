import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard_fixture():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_init(keyboard_fixture):
    assert keyboard_fixture.name == 'Dark Project KD87A'
    assert keyboard_fixture.price == 9600
    assert keyboard_fixture.quantity == 5
    assert keyboard_fixture.language == 'EN'


def test_switch_language_mixin_change_lang(keyboard_fixture):
    keyboard_fixture.change_lang()
    assert keyboard_fixture.language == 'RU'
    keyboard_fixture.change_lang()
    assert keyboard_fixture.language == 'EN'

