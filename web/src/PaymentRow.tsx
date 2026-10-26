export function PaymentRow({ id, amount, status }: { id: string; amount: string; status: string }) {
  return (
    <tr>
      <td>{id}</td>
      <td>{amount}</td>
      <td>{status}</td>
    </tr>
  )
}
