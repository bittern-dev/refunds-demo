import type { components } from './schema.gen'

export type Refund = components['schemas']['Refund']

export async function createRefund(paymentId: string, amount: number): Promise<Refund> {
  const res = await fetch(`/payments/${paymentId}/refunds?amount=${amount}`, { method: 'POST' })
  if (!res.ok) throw new Error(await res.text())
  return res.json()
}
