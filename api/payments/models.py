from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Payment:
    id: str
    customer_id: str
    amount: Decimal
    captured: Decimal = Decimal(0)
    refunded: Decimal = Decimal(0)
    status: str = "pending"
    events: list[str] = field(default_factory=list)


@dataclass
class Refund:
    id: str
    payment_id: str
    amount: Decimal
    status: str = "pending"  # pending, sent or failed

    def mark_sent(self) -> None:
        self.status = "sent"

    def mark_failed(self) -> None:
        self.status = "failed"
