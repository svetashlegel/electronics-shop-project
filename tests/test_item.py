from src.item import Item


def test_calculate_total_price(laptop):
    assert laptop.calculate_total_price() == 400000


def test_apply_discount(laptop):
    laptop.pay_rate = 0.5
    laptop.apply_discount()
    assert laptop.price == 20000


def test_name(laptop):
    assert laptop.name == 'laptop'

    laptop.name = 'ноутбук'
    assert laptop.name == 'ноутбук'

    laptop.name = "SuperLaptop"
    assert laptop.name == 'ноутбук'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 8


def test_string_to_number():
    assert Item.string_to_number('845.3') == 845
