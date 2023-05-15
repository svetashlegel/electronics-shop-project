from src.item import Item


def test_calculate_total_price(laptop):
    assert laptop.calculate_total_price() == 400000


def test_apply_discount(laptop):
    laptop.pay_rate = 0.5
    laptop.apply_discount()
    assert laptop.price == 20000
