'use client'

import { motion } from 'framer-motion'

const agents = ['Planner Agent', 'Research Agent', 'Executor Agent', 'Memory Agent']

export function AgentStatusPanel() {
  return (
    <section className="glass p-4">
      <h2 className="text-lg font-semibold mb-3">Agent Status</h2>
      <div className="space-y-2">
        {agents.map((agent, idx) => (
          <motion.div
            key={agent}
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: idx * 0.1 }}
            className="flex justify-between text-sm bg-white/5 rounded-lg p-2"
          >
            <span>{agent}</span>
            <span className="text-emerald-300">Ready</span>
          </motion.div>
        ))}
      </div>
    </section>
  )
}
