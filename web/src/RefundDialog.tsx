import { useState } from 'react'
import { createRefund } from './api/refunds'

export function RefundDialog({ paymentId, refundable, onDone }: { paymentId: string; refundable: number; onDone: () => void }) {
  const [amount, setAmount] = useState(refundable)
  const [error, setError] = useState<string>()
  return (
    <form
      onSubmit={async (e) => {
        e.preventDefault()
        try {
          await createRefund(paymentId, amount)
          onDone()
        } catch (err) {
          setError(String(err))
        }
      }}
    >
      <label>
        Amount to refund
        <input type="number" min={0.01} max={refundable} step={0.01} value={amount} onChange={(e) => setAmount(Number(e.target.value))} />
      </label>
      {error && <p role="alert">{error}</p>}
      <button type="submit">Refund £{amount.toFixed(2)}</button>
    </form>
  )
}
