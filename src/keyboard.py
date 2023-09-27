from src.item import Item


class SwitchLanguageMixin:
    pass


class Keyboard(Item, SwitchLanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        """Создание экземпляра класса Keyboard.

        :param name, price � quantit подтягивается через функцию super из класса Item.
        :protected param language - язык раскладки клавиатуры(по умолчанию 'EN')."""
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        """Геттер защищенного атрибута language"""
        return self._language
