import pytest
from sweet_shop.shop import SweetShop
from sweet_shop.sweet import Sweet

def test_add_sweet():
    """Tests if a new sweet can be successfully added to the shop."""
    shop = SweetShop()
    sweet_to_add = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    shop.add_sweet(sweet_to_add)
    assert len(shop.get_all_sweets()) == 1
    assert shop.get_all_sweets()[0].id == 1001

def test_delete_sweet():
    """Tests if a sweet can be successfully deleted from the shop."""
    shop = SweetShop()
    sweet_to_add = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    shop.add_sweet(sweet_to_add)
    
    shop.delete_sweet(1001)
    assert len(shop.get_all_sweets()) == 0
    
def test_sweet_by_name():
    """Tests the search functionality for finding sweets by their name."""
    shop = SweetShop()
    sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    sweet2 = Sweet(id=1002, name="Gulab Jamun", category="Fried", price=30, quantity=15)
    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    
    res = shop.get_sweet_by_name("Kaju Katli")
    assert len(res) == 1
    
def test_sweet_by_category():
    """Tests the search functionality for finding sweets by their category."""
    shop = SweetShop()
    sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    sweet2 = Sweet(id=1002, name="Gulab Jamun", category="Fried", price=30, quantity=15)
    sweet3 = Sweet(id=1003, name="Rasgulla", category="Fried", price=25, quantity=10)
    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    shop.add_sweet(sweet3)
    
    res = shop.get_sweet_by_category("Fried")   
    assert len(res) == 2 
    
def test_sweet_by_price():
    """Tests the search functionality for finding sweets within a price range."""
    shop = SweetShop()
    sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    sweet2 = Sweet(id=1002, name="Gulab Jamun", category="Fried", price=30, quantity=15)
    sweet3 = Sweet(id=1003, name="Rasgulla", category="Fried", price=25, quantity=10)
    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    shop.add_sweet(sweet3)
    
    res = shop.get_sweet_by_price(min_price=20, max_price=30)   
    assert len(res) == 2    

def test_purchase_sweet():
    """Tests if purchasing a sweet correctly decreases its stock quantity."""
    shop = SweetShop()
    sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    shop.add_sweet(sweet1)
    
    # Simulate purchasing 15 sweets
    shop.purchase_sweet(1001, 15)
    
    # Verify the quantity is updated
    newsweet = shop.get_sweet_by_id(1001)
    assert newsweet.quantity == 5    
    
def test_restock_sweet():
    """Tests if restocking a sweet correctly increases its stock quantity."""
    shop = SweetShop()
    sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
    shop.add_sweet(sweet1)
    
    shop.restock_sweet(1001, 10)
    newsweet = shop.get_sweet_by_id(1001)
    assert newsweet.quantity == 30  # Initial quantity was 20, after restock it should be 30