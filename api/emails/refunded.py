from decimal import Decimal

from api.emails.send import send


def send_refunded_email(customer_id: str, amount: Decimal) -> None:
    send(
        to=customer_id,
        subject="Your refund is on its way",
        body=f"We've refunded £{amount:.2f}. It can take 3-5 working days to reach your account.",
    )
