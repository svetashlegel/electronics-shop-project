import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def laptop():
    return Item("laptop", 40000, 10)


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone1():
    return Phone('phone', 20000, 10, 2)
