import pytest
from src.item import Item


@pytest.fixture
def laptop():
    return Item("laptop", 40000, 10)

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)
