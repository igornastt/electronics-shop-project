import pytest
from src.keyboard import Keyboard


def test_init():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == 'EN'
    with pytest.raises(AttributeError):
        kb.language = 'RU'

def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"

    with pytest.raises(AttributeError):
        kb.language = 'CH'
        # AttributeError: property 'language' of 'KeyBoard' object has no setter
