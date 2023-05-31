from src.item import Item


class MixinLang:
    """
        Класс дополнительного функционала по хранению и изменению раскладки клавиатуры.
    """

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        """Возвращает язык раскладки"""
        return self.__language

    def change_lang(self):
        """Производит смену языка раскладки"""
        if self.language == "EN":
            self.__language = "RU"
        elif self.language == "RU":
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLang):
    """
    Класс для представления товара "клавиатура" в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
               Создание экземпляра класса Phone.

               :param name: Название товара.
               :param price: Цена за единицу товара.
               :param quantity: Количество товара в магазине.

               :param language: поддерживаемый язык.
               """
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"
