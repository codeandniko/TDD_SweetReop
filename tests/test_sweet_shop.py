import pytest
from sweet_shop import SweetShop
from sweet_shop import Sweet

def test_add_sweet():
    shop=SweetShop()
    sweet_to_add=Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    shop.add_sweet(sweet_to_add)
    assert len(shop.get_all_sweets()) == 1
    assert shop.get_all_sweets()[0].id == 1001


def test_delete_sweet():
    shop = SweetShop()
    sweet_to_add = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    shop.add_sweet(sweet_to_add)
    
    shop.delete_sweet(1001)
    assert len(shop.get_all_sweets()) == 0
    

def test_sweet_by_name():
    shop = SweetShop()
    sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    sweet2 = Sweet(id=1002, name="Gulab Jamun", category="Fried", price=30, quantity=15)
    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    res= shop.get_sweet_by_name("Kaju Katli")
    assert len(res) == 1
    