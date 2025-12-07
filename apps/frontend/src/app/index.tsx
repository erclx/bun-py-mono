import { useEffect, useState } from 'react'

interface Item {
  item_id: number
}

export const App = () => {
  const [item, setItem] = useState<Item | null>(null)

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/items/12`)
      .then((res) => res.json())
      .then((data) => setItem(data))
      .catch((err) => console.error('Error:', err))
  }, [])

  return (
    <div>
      <h1>My React App</h1>
      {item && <p>Item ID from backend: {item.item_id}</p>}
    </div>
  )
}
