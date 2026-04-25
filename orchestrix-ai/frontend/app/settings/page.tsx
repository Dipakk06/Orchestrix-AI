export default function SettingsPage() {
  return (
    <main className="p-6 max-w-3xl mx-auto">
      <section className="glass p-6">
        <h1 className="text-2xl font-semibold mb-4">Settings</h1>
        <div className="space-y-3 text-sm">
          <p>Default Model: <span className="text-cyan-300">gemma3 (Ollama)</span></p>
          <p>Speech to Text: Whisper</p>
          <p>Text to Speech: pyttsx3 / Coqui-ready architecture</p>
          <p>Memory Backend: ChromaDB</p>
        </div>
      </section>
    </main>
  )
}
