import pytest
from sweet_shop import SweetShop
from sweet_shop import Sweet

def test_add_sweet():
    shop=SweetShop()
    sweet_to_add=Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    shop.add_sweet(sweet_to_add)
    assert len(shop.get_all_sweets()) == 1
    assert shop.get_all_sweets()[0].id == 1001
