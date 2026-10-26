# Plan: partial refunds (issue #1)

1. Model: add `refunded` to Payment, a Refund dataclass with status.
2. `refund()` in api/payments/refund.py: validate amount, record in ledger, call bank.
3. Bank failures: background retry job (api/jobs) so customers aren't left waiting.
4. Email the customer on success.
5. Route + web dialog + generated client.
6. Tests for amounts.

Open questions: finance export format? (skipped for now)
