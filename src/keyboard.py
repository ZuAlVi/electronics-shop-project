from src.item import Item


class SwitchLanguageMixin:

    def change_lang(self):
        """Метод позволяет изменять значение защищенного
        атрибута language c 'EN' на 'RU' и наоборот."""
        if self.language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, SwitchLanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        """Создание экземпляра класса Keyboard.

        :param name, price и quantity подтягивается через функцию super из класса Item.
        :protected param language - язык раскладки клавиатуры(по умолчанию 'EN')."""
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        """Геттер защищенного атрибута language"""
        return self._language
