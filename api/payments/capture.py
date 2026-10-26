from decimal import Decimal

from api.payments.models import Payment


def capture(payment: Payment, amount: Decimal) -> Payment:
    if amount > payment.amount - payment.captured:
        raise ValueError("can't capture more than was authorised")
    payment.captured += amount
    payment.status = "captured"
    payment.events.append(f"captured {amount}")
    return payment
