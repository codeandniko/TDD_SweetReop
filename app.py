from flask import Flask, jsonify, render_template, request
from typing import List, Optional

# --- Data Model ---
# This class represents a single sweet. It's needed for the SweetShop to work.
class Sweet:
    _id_counter = 1

    def __init__(self, name: str, category: str, price: float, quantity: int):
        self.id = Sweet._id_counter
        Sweet._id_counter += 1
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    # This method helps in converting the object to a dictionary for JSON responses
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }

# --- Business Logic (Your provided shop.py class) ---
class SweetShop:
    """Manages the inventory and operations of a sweet shop."""

    def __init__(self):
        """Initializes a new, empty sweet shop."""
        self._sweets = {}

    def add_sweet(self, sweet: Sweet):
        """Adds a sweet to the shop's inventory."""
        self._sweets[sweet.id] = sweet

    def get_all_sweets(self) -> List[Sweet]:
        """Returns a list of all sweets currently in the shop."""
        return list(self._sweets.values())

    def get_sweet_by_id(self, sweet_id: int) -> Optional[Sweet]:
        """Finds and returns a single sweet by its unique ID."""
        return self._sweets.get(sweet_id)

    def delete_sweet(self, sweet_id: int):
        """Removes a sweet from the shop by its ID."""
        if sweet_id in self._sweets:
            del self._sweets[sweet_id]
        else:
            raise ValueError(f"Sweet with ID {sweet_id} not found.")

    def update_sweet(self, sweet_id: int, name: str, category: str, price: float, quantity: int) -> Sweet:
        """Updates the details of an existing sweet."""
        sweet = self.get_sweet_by_id(sweet_id)
        if sweet:
            sweet.name = name
            sweet.category = category
            sweet.price = price
            sweet.quantity = quantity
            return sweet
        else:
            raise ValueError(f"Sweet with ID {sweet_id} not found.")

    def purchase_sweet(self, sweet_id: int, want: int):
        """Processes the purchase of a sweet, decreasing its stock."""
        sweet = self.get_sweet_by_id(sweet_id)
        if not sweet:
            raise ValueError(f"Sweet with ID {sweet_id} not found.")
        if sweet.quantity < want:
            raise ValueError(f"Not enough stock for {sweet.name}. Available: {sweet.quantity}, Requested: {want}")
        sweet.quantity -= want

    def restock_sweet(self, sweet_id: int, add: int):
        """Increases the stock quantity of a specific sweet."""
        sweet = self.get_sweet_by_id(sweet_id)
        if not sweet:
            raise ValueError(f"Sweet with ID {sweet_id} not found.")
        sweet.quantity += add

# --- Flask Application Setup ---
# By default, Flask looks for templates in a folder named "templates".
# This is the standard and recommended practice.
app = Flask(__name__)
shop = SweetShop()

# --- Initial Data ---
# Populate the shop with some default sweets for demonstration
def add_initial_data():
    shop.add_sweet(Sweet(name="Chocolate Bar", category="Chocolate", price=2.50, quantity=50))
    shop.add_sweet(Sweet(name="Gummy Bears", category="Gummy", price=5.00, quantity=100))
    shop.add_sweet(Sweet(name="Lollipop", category="Hard Candy", price=1.00, quantity=200))
    shop.add_sweet(Sweet(name="Caramel Chew", category="Caramel", price=0.75, quantity=150))
    shop.add_sweet(Sweet(name="Sour Patch Kids", category="Sour", price=4.50, quantity=15))

add_initial_data()

# --- HTML Rendering Route ---
@app.route('/')
def index():
    """Renders the main HTML page for the shop frontend."""
    return render_template('index.html')

# --- API Endpoints ---
@app.route('/api/sweets', methods=['GET'])
def get_sweets():
    """API endpoint to get all sweets."""
    all_sweets = shop.get_all_sweets()
    return jsonify([s.to_dict() for s in all_sweets])

@app.route('/api/sweets', methods=['POST'])
def create_sweet():
    """API endpoint to add a new sweet."""
    data = request.get_json()
    if not all(k in data for k in ['name', 'category', 'price', 'quantity']):
        return jsonify({"error": "Missing data"}), 400
    
    try:
        new_sweet = Sweet(
            name=data['name'],
            category=data['category'],
            price=float(data['price']),
            quantity=int(data['quantity'])
        )
        shop.add_sweet(new_sweet)
        return jsonify(new_sweet.to_dict()), 201
    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid data format: {e}"}), 400


@app.route('/api/sweets/<int:sweet_id>', methods=['GET'])
def get_sweet(sweet_id):
    """API endpoint to get a single sweet by its ID."""
    sweet = shop.get_sweet_by_id(sweet_id)
    if sweet:
        return jsonify(sweet.to_dict())
    return jsonify({"error": "Sweet not found"}), 404

@app.route('/api/sweets/<int:sweet_id>', methods=['PUT'])
def update_sweet_route(sweet_id):
    """API endpoint to update an existing sweet."""
    data = request.get_json()
    if not all(k in data for k in ['name', 'category', 'price', 'quantity']):
        return jsonify({"error": "Missing data"}), 400

    try:
        updated_sweet = shop.update_sweet(
            sweet_id,
            name=data['name'],
            category=data['category'],
            price=float(data['price']),
            quantity=int(data['quantity'])
        )
        return jsonify(updated_sweet.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except (TypeError) as e:
        return jsonify({"error": f"Invalid data format: {e}"}), 400


@app.route('/api/sweets/<int:sweet_id>', methods=['DELETE'])
def delete_sweet_route(sweet_id):
    """API endpoint to delete a sweet."""
    try:
        shop.delete_sweet(sweet_id)
        return '', 204 # No Content
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/sweets/<int:sweet_id>/purchase', methods=['POST'])
def purchase_sweet_route(sweet_id):
    """API endpoint to purchase a quantity of a sweet."""
    data = request.get_json()
    if 'quantity' not in data:
        return jsonify({"error": "Missing quantity"}), 400
    
    try:
        quantity_to_buy = int(data['quantity'])
        if quantity_to_buy <= 0:
             return jsonify({"error": "Quantity must be positive"}), 400
        shop.purchase_sweet(sweet_id, quantity_to_buy)
        return jsonify({"success": True, "message": f"Purchase successful."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400 # Could be 404 or 400 depending on error

@app.route('/api/sweets/<int:sweet_id>/restock', methods=['POST'])
def restock_sweet_route(sweet_id):
    """API endpoint to restock a quantity of a sweet."""
    data = request.get_json()
    if 'quantity' not in data:
        return jsonify({"error": "Missing quantity"}), 400

    try:
        quantity_to_add = int(data['quantity'])
        if quantity_to_add <= 0:
             return jsonify({"error": "Quantity must be positive"}), 400
        shop.restock_sweet(sweet_id, quantity_to_add)
        return jsonify({"success": True, "message": f"Restock successful."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
