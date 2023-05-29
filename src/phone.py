from src.item import Item


class Phone(Item):
    """
    Класс для представления товара в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
               Создание экземпляра класса Phone.

               :param name: Название товара.
               :param price: Цена за единицу товара.
               :param quantity: Количество товара в магазине.

               :param sim_quantity: Кол-во симкарт.
               """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """Возвращает кол-во сим-карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_value):
        """Устанавливает новое кол-во сим-карт"""
        if isinstance(new_value, int) and new_value > 0:
            self.__number_of_sim = new_value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
