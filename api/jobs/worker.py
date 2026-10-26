from api.jobs.base import Job, RetryLater, backoff
from api.payments import bank
from api.store import refunds


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
        else:
            raise RetryLater(backoff(self.tries))

    def on_give_up(self) -> None:
        refunds[self.refund_id].mark_failed()
