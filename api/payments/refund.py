import uuid
from decimal import Decimal

from api.emails.refunded import send_refunded_email
from api.jobs.queue import enqueue
from api.jobs.worker import RetryRefund
from api.payments import bank
from api.payments.models import Payment, Refund
from api.store import ledger, refunds


class RefundTooLarge(ValueError):
    pass


def refund(payment: Payment, amount: Decimal) -> Refund:
    """Refunds part (or all) of what was captured."""
    if amount <= 0:
        raise ValueError("refund must be positive")
    if amount > payment.captured - payment.refunded:
        raise RefundTooLarge(amount)

    r = Refund(id=str(uuid.uuid4()), payment_id=payment.id, amount=amount)
    refunds[r.id] = r
    payment.refunded += amount
    payment.events.append(f"refunded {amount}")
    ledger.record(payment.id, "refund", -amount)

    if bank.send(r):
        r.mark_sent()
        send_refunded_email(payment.customer_id, amount)
    else:
        enqueue(RetryRefund(r.id))
    return r
