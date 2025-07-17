from typing import List, Optional
from .sweet import Sweet

class SweetShop:
    """Manages the inventory and operations of a sweet shop."""

    def __init__(self):
        """Initializes a new, empty sweet shop."""
        self._sweets = {}
            
    def add_sweet(self, sweet: Sweet):
        """
        Adds a sweet to the shop's inventory.
        If a sweet with the same ID already exists, it will be overwritten.
        """
        self._sweets[sweet.id] = sweet 
              
    def get_all_sweets(self) -> List[Sweet]:
        """Returns a list of all sweets currently in the shop."""
        return list(self._sweets.values())
    
    def get_sweet_by_id(self, sweet_id: int) -> Optional[Sweet]:
        """
        Finds and returns a single sweet by its unique ID.
        
        Args:
            sweet_id: The ID of the sweet to find.
        
        Returns:
            The Sweet object if found, otherwise None.
        """
        return self._sweets.get(sweet_id, None)        
    
    def delete_sweet(self, sweet_id: int):
        """
        Removes a sweet from the shop by its ID.
        If the ID is not found, it does nothing.
        """
        if sweet_id in self._sweets:
            del self._sweets[sweet_id]
    
    def get_sweet_by_name(self, name: str) -> List[Sweet]:
        """
        Searches for sweets by name.
        
        Returns:
            A list of sweets matching the name, or an empty list if none match.
        """
        return [sweet for sweet in self._sweets.values() if sweet.name == name]       
    
    def get_sweet_by_category(self, category: str) -> List[Sweet]:
        """
        Searches for sweets by category.
        
        Returns:
            A list of sweets matching the category, or an empty list if none match.
        """
        return [sweet for sweet in self._sweets.values() if sweet.category == category]  
    
    def get_sweet_by_price(self, min_price: float, max_price: float) -> List[Sweet]:
        """
        Finds all sweets within a given price range (inclusive).
        
        Returns:
            A list of sweets within the price range, or an empty list.
        """
        return [sweet for sweet in self._sweets.values() if min_price <= sweet.price <= max_price]
    
    def purchase_sweet(self, sweet_id: int, want: int):
        """
        Processes the purchase of a sweet, decreasing its stock.
        
        Raises:
            ValueError: If the sweet ID is not found or if the stock is insufficient.
        """
        if sweet_id in self._sweets:
            sweet = self._sweets[sweet_id]
            if sweet.quantity >= want:
                sweet.quantity -= want
            else:
                raise ValueError(f"Not enough quantity for {sweet.name}. Available: {sweet.quantity}, Requested: {want}")
        else:
            raise ValueError(f"Sweet with ID {sweet_id} not found.")
    
    def restock_sweet(self, sweet_id: int, add: int):
        """
        Increases the stock quantity of a specific sweet.
        
        Raises:
            ValueError: If the sweet ID is not found.
        """
        if sweet_id in self._sweets:
            sweet = self._sweets[sweet_id]
            sweet.quantity += add
        else:
            raise ValueError(f"Sweet with ID {sweet_id} not found.")