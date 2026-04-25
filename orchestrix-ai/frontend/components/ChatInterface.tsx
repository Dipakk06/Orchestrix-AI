'use client'

import { Mic, Send } from 'lucide-react'
import ReactMarkdown from 'react-markdown'
import { useState } from 'react'

import { saveMemory, searchMemory, streamChat } from '@/lib/api'
import type { ChatMessage } from '@/types'

const USER_ID = 'demo-user'

export function ChatInterface({ onLog, onMemories }: { onLog: (entry: string) => void; onMemories: (entries: string[]) => void }) {
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const send = async (text: string) => {
    if (!text.trim()) return

    setLoading(true)
    setInput('')
    setMessages((prev) => [...prev, { role: 'user', content: text }, { role: 'assistant', content: '' }])
    onLog(`chat: sending message => ${text}`)

    await streamChat(USER_ID, text, (chunk) => {
      setMessages((prev) => {
        const copy = [...prev]
        const last = copy[copy.length - 1]
        if (last?.role === 'assistant') {
          last.content += chunk
        }
        return copy
      })
    })

    await saveMemory(USER_ID, text)
    const memoryResult = await searchMemory(USER_ID, text)
    const memories = (memoryResult.items ?? []).map((item: { content: string }) => item.content)
    onMemories(memories)
    onLog(`memory: ${memories.length} related records`)
    setLoading(false)
  }

  const startMic = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    const recorder = new MediaRecorder(stream)
    const chunks: BlobPart[] = []

    recorder.ondataavailable = (event) => chunks.push(event.data)
    recorder.onstop = async () => {
      const blob = new Blob(chunks, { type: 'audio/wav' })
      const form = new FormData()
      form.append('file', blob, 'input.wav')

      const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000/api'}/voice/stt`, {
        method: 'POST',
        body: form,
      })
      const data = await response.json()
      setInput(data.text ?? '')
      onLog('voice: speech converted to text')
    }

    recorder.start()
    setTimeout(() => recorder.stop(), 3000)
  }

  return (
    <section className="glass p-4 flex flex-col h-[70vh]">
      <h2 className="text-lg font-semibold mb-3">AI Chat Assistant</h2>
      <div className="flex-1 overflow-auto space-y-3 mb-3 pr-1">
        {messages.map((message, idx) => (
          <article key={idx} className={`p-3 rounded-xl ${message.role === 'user' ? 'bg-cyan-500/20' : 'bg-purple-500/20'}`}>
            <p className="text-xs mb-1 uppercase opacity-70">{message.role}</p>
            <div className="prose prose-invert max-w-none">
              <ReactMarkdown>{message.content || (loading && idx === messages.length - 1 ? '...' : '')}</ReactMarkdown>
            </div>
          </article>
        ))}
      </div>
      <div className="flex gap-2">
        <button onClick={startMic} className="px-3 rounded-xl bg-white/10 hover:bg-white/20">
          <Mic size={18} />
        </button>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 bg-black/20 rounded-xl px-3 py-2 outline-none border border-white/10"
          placeholder="Ask Orchestrix AI anything..."
        />
        <button onClick={() => send(input)} disabled={loading} className="px-4 rounded-xl bg-gradient-to-r from-blue-500 to-purple-600">
          <Send size={18} />
        </button>
      </div>
    </section>
  )
}
