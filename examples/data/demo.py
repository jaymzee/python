"""dataclass makes it easier to create simple data classes"""

from dataclasses import dataclass

@dataclass
class InventoryItem:
    """a item in the inventory"""

    name: str
    unit_price: float
    quantity_on_hand: int

    def total_cost(self) -> float:
        """Return the total cost"""
        return self.unit_price * self.quantity_on_hand


Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    """Return Vector scaled by scalar"""
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])

print(new_vector)
