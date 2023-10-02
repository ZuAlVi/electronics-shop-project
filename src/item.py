import csv

from src.errors import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        """Метод возвращает информацию для разработчиков."""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Метод возвращает информацию для пользователя."""
        return self.__name

    def __add__(self, other):
        """Метод позволяет складывать экземпляры классов Item и Phone по атрибуту quantity."""
        from src.phone import Phone
        if isinstance(self, (Item, Phone)) and isinstance(other, (Item, Phone)):
            return int(self.quantity) + int(other.quantity)

    @property
    def name(self):
        """Геттер приватного атрибута __name"""
        return self.__name

    @name.setter
    def name(self, name):
        """Сеттер приватного атрибута __name"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        """Класс метод производит инициализацию экземпляров класса
        из файлов .csv. Если файл не найден или поврежден выводится сообщение."""
        Item.all = []
        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                len_reader = len(reader.fieldnames)
                if len_reader != 3:
                    raise InstantiateCSVError
                for row in reader:
                    name = row['name']
                    price = Item.string_to_number(row['price'])
                    quantity = Item.string_to_number(row['quantity'])
                    Item(name, price, quantity)
        except InstantiateCSVError as error:
            print(error.message)
            raise  # для проверки через pytest.raises
        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv')
            raise  # для проверки через pytest.raises

    @staticmethod
    def string_to_number(string: str):
        """Статик метод принимающий на вход строку.
        Если строка состоит из цифр, возвращает число.
        Иначе None"""
        if '.' in string:
            temp = string[:string.find('.')]
            if temp.isdigit():
                return int(temp)
            return None
        elif string.isdigit():
            return int(string)

# Item.instantiate_from_csv()
