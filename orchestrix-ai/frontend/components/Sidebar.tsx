'use client'

import { Bot, Brain, Settings, Wrench } from 'lucide-react'

const items = [
  { label: 'Chat', icon: Bot },
  { label: 'Memory', icon: Brain },
  { label: 'Tools', icon: Wrench },
  { label: 'Settings', icon: Settings },
]

export function Sidebar() {
  return (
    <aside className="glass w-full lg:w-64 p-4">
      <h1 className="text-2xl font-semibold text-transparent bg-clip-text bg-gradient-to-r from-cyan-300 to-purple-400 mb-6">Orchestrix AI</h1>
      <nav className="space-y-3">
        {items.map(({ label, icon: Icon }) => (
          <button key={label} className="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-white/10 transition">
            <Icon size={18} />
            <span>{label}</span>
          </button>
        ))}
      </nav>
    </aside>
  )
}
