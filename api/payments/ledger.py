from decimal import Decimal


class Ledger:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, Decimal]] = []

    def record(self, payment_id: str, kind: str, amount: Decimal) -> None:
        self.rows.append((payment_id, kind, amount))
