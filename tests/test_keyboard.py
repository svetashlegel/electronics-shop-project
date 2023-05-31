import pytest


def test_class_str(keyboard1):
    assert str(keyboard1) == 'keyboard'


def test_class_repr(keyboard1):
    assert repr(keyboard1) == "Keyboard('keyboard', 5000, 15, EN)"


def test_language(keyboard1):
    assert keyboard1.language == "EN"
    keyboard1.change_lang()
    assert keyboard1.language == "RU"
    keyboard1.change_lang().change_lang()
    assert keyboard1.language == "RU"


def test_language_setter(keyboard1):
    with pytest.raises(AttributeError):
        keyboard1.language = "CH"
