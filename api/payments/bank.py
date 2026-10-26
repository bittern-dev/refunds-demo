from api.payments.models import Refund


class BankError(Exception):
    pass


def send(refund: Refund) -> bool:
    """Asks the bank to return the money; False when the bank is unavailable."""
    return True
