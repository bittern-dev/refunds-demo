from api.jobs.base import Job, RetryLater, backoff
from api.emails.refunded import send_refunded_email
from api.payments import bank
from api.store import payments, refunds


class RetryRefund(Job):
    """Retries a refund the bank couldn't take at first."""

    attempts = 5

    def __init__(self, refund_id: str) -> None:
        super().__init__()
        self.refund_id = refund_id

    def run(self) -> None:
        refund = refunds[self.refund_id]
        if bank.send(refund):
            refund.mark_sent()
            send_refunded_email(payments[refund.payment_id].customer_id, refund.amount)
        else:
            raise RetryLater(backoff(self.tries))

    def on_give_up(self) -> None:
        refunds[self.refund_id].mark_failed()
