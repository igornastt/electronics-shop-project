"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_items():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000
    assert isinstance(item1, Item)

    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000
