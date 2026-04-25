'use client'

import { useEffect, useState } from 'react'

import { AgentStatusPanel } from '@/components/AgentStatusPanel'
import { ChatInterface } from '@/components/ChatInterface'
import { MemoryViewer } from '@/components/MemoryViewer'
import { Sidebar } from '@/components/Sidebar'
import { ToolLogs } from '@/components/ToolLogs'
import { fetchTools } from '@/lib/api'

export default function Dashboard() {
  const [logs, setLogs] = useState<string[]>(['system: dashboard initialized'])
  const [memories, setMemories] = useState<string[]>([])

  useEffect(() => {
    fetchTools().then((data) => {
      const names = (data.tools ?? []).map((t: { name: string }) => t.name).join(', ')
      setLogs((prev) => [`tools: loaded => ${names}`, ...prev])
    })
  }, [])

  return (
    <main className="p-4 lg:p-6 grid grid-cols-1 lg:grid-cols-[256px_1fr_340px] gap-4">
      <Sidebar />
      <ChatInterface onLog={(entry) => setLogs((prev) => [entry, ...prev].slice(0, 20))} onMemories={setMemories} />
      <div className="space-y-4">
        <AgentStatusPanel />
        <ToolLogs logs={logs} />
        <MemoryViewer memories={memories} />
      </div>
    </main>
  )
}
