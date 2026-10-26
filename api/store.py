from api.payments.ledger import Ledger
from api.payments.models import Payment

payments: dict[str, Payment] = {}
ledger = Ledger()
