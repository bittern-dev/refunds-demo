from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Payment:
    id: str
    customer_id: str
    amount: Decimal
    captured: Decimal = Decimal(0)
    status: str = "pending"
    events: list[str] = field(default_factory=list)
