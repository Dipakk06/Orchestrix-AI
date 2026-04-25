'use client'

export function MemoryViewer({ memories }: { memories: string[] }) {
  return (
    <section className="glass p-4">
      <h2 className="text-lg font-semibold mb-3">Memory Viewer</h2>
      <ul className="space-y-2 text-sm">
        {memories.map((memory, idx) => (
          <li key={`${memory}-${idx}`} className="rounded-lg bg-white/5 p-2">
            {memory}
          </li>
        ))}
      </ul>
    </section>
  )
}
