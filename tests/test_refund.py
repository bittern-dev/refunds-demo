from decimal import Decimal

import pytest

from api.payments.models import Payment
from api.payments.refund import RefundTooLarge, refund


def captured(amount: int) -> Payment:
    return Payment("p1", "c1", Decimal(amount), captured=Decimal(amount), status="captured")


def test_refund_part_of_a_payment():
    p = captured(100)
    r = refund(p, Decimal(30))
    assert (r.amount, r.status, p.refunded) == (30, "sent", 30)


def test_refunds_never_exceed_what_was_captured():
    p = captured(100)
    refund(p, Decimal(80))
    with pytest.raises(RefundTooLarge):
        refund(p, Decimal(30))
