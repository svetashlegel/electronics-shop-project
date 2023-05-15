import pytest
from src.item import Item


@pytest.fixture
def laptop():
    return Item("laptop", 40000, 10)