from api.payments.ledger import Ledger
from api.payments.models import Payment, Refund

payments: dict[str, Payment] = {}
refunds: dict[str, Refund] = {}
ledger = Ledger()
