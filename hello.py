from dataclasses import dataclass

class Student(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int
