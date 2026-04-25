'use client'

export function ToolLogs({ logs }: { logs: string[] }) {
  return (
    <section className="glass p-4">
      <h2 className="text-lg font-semibold mb-3">Tool Execution Logs</h2>
      <div className="space-y-2 max-h-40 overflow-auto text-xs font-mono">
        {logs.map((log, index) => (
          <div key={`${log}-${index}`} className="bg-black/30 p-2 rounded-lg">
            {log}
          </div>
        ))}
      </div>
    </section>
  )
}
