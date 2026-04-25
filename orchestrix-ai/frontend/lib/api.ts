const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000/api'

export async function streamChat(userId: string, message: string, onChunk: (chunk: string) => void) {
  const res = await fetch(`${API_BASE}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user_id: userId, message }),
  })

  if (!res.body) throw new Error('No stream body returned')
  const reader = res.body.getReader()
  const decoder = new TextDecoder()

  while (true) {
    const { done, value } = await reader.read()
    if (done) break
    onChunk(decoder.decode(value, { stream: true }))
  }
}

export async function fetchTools() {
  const res = await fetch(`${API_BASE}/tools`)
  return res.json()
}

export async function saveMemory(user_id: string, content: string) {
  return fetch(`${API_BASE}/memory/save`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user_id, content, importance: 6 }),
  }).then((r) => r.json())
}

export async function searchMemory(user_id: string, query: string) {
  const p = new URLSearchParams({ user_id, query, limit: '5' })
  return fetch(`${API_BASE}/memory/search?${p}`).then((r) => r.json())
}
