from typing import List, Optional
from .sweet import Sweet

class SweetShop:
    def __init__(self):
        self._sweets = {}
        
    def add_sweet(self, sweet: Sweet):
        self._sweets[sweet.id] = sweet
    
    def get_all_sweets(self) -> List[Sweet]:
        return list(self._sweets.values())
    
    def get_sweet_by_id(self, sweet_id: int) -> Optional[Sweet]:
        return self._sweets.get(sweet_id, None)        
    
    def delete_sweet(self, sweet_id: int):
        if sweet_id in self._sweets:
            del self._sweets[sweet_id]
    
    def  get_sweet_by_name(self, name: str) -> List[Sweet]:
        return [sweet for sweet in self._sweets.values() if sweet.name == name]       
    
    def get_sweet_by_category(self, category: str) -> List[Sweet]:
        return [sweet for sweet in self._sweets.values() if sweet.category == category]  
    
    def get_sweet_by_price(self, min_price: float, max_price: float) -> List[Sweet]:
        return [sweet for sweet in self._sweets.values() if min_price <= sweet.price <= max_price]