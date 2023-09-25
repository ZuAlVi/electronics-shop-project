from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone.

        :param name, price и quantity подтягиваются через функцию super из класса Item.
        :param number_of_sim - количество физических SIM-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Метод возвращает информацию для разработчиков."""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """Геттер приватного атрибута __number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Сеттер приватного атрибута __number_of_sim
        param value не может быть меньше либо равен 0.
        """
        if value <= 0 and isinstance(value, int):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = value
