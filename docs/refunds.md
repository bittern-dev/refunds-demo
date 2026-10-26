# Refunds

`POST /payments/{id}/refunds?amount=…` refunds part or all of a captured payment. A refund can never
exceed what was captured minus what was already refunded.

If the bank can't take a refund straight away, it's retried in the background (up to 5 times, with
backoff) and marked failed if it still doesn't go through.
