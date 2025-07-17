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