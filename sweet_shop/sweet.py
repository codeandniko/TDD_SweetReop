from dataclasses import dataclass, field

@dataclass
class Sweet:
    id: int
    name: str
    category: str
    price: float
    quantity: int = field(default=0)