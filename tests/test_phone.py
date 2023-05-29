import pytest

from src.phone import Phone


def test_class_str(phone1):
    assert str(phone1) == 'phone'


def test_class_repr(phone1):
    assert repr(phone1) == "Phone('phone', 20000, 10, 2)"


def test_number_of_sim(phone1):
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1


def test_num_of_sim_exception(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
