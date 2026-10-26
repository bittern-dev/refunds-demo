from decimal import Decimal

from fastapi import APIRouter

from api.payments.capture import capture
from api.payments.refund import refund
from api.store import payments

router = APIRouter()


@router.post("/payments/{payment_id}/capture")
def capture_payment(payment_id: str, amount: Decimal):
    return capture(payments[payment_id], amount)


@router.post("/payments/{payment_id}/refunds")
def refund_payment(payment_id: str, amount: Decimal):
    return refund(payments[payment_id], amount)
