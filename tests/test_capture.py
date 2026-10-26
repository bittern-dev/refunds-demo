from decimal import Decimal

import pytest

from api.payments.capture import capture
from api.payments.models import Payment


def test_capture_up_to_the_authorised_amount():
    p = capture(Payment("p1", "c1", Decimal(100)), Decimal(60))
    assert p.captured == 60
    with pytest.raises(ValueError):
        capture(p, Decimal(50))
