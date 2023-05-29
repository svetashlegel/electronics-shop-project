import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    items_data = r'C:\Users\Sveta\PycharmProjects\electronics-shop-project\src\items.csv'

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
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return str(self.name)

    @property
    def name(self):
        """Возвращает наименование товара"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Устанавливает новое наименование товара (не длиннее 10 символов)"""
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file=items_data):
        """Инициализирует экземпляры класса Item данными из файла"""
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, price, quantity = row['name'], row['price'], row['quantity']
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """Возвращает число из числа-строки"""
        return int(float(string))

    def __add__(self, other):
        """Реализует возможность сложения экземпляров класса Phone и Item (сложение по количеству товара в магазине)"""
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise ValueError('Складывать можно только объекты Item и дочерние от них.')
