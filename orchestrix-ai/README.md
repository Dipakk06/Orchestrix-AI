# Orchestrix AI

Production-ready MVP for an advanced AI assistant platform with chat, tools, memory, voice, and agentic execution.

## Stack
- Frontend: Next.js 15 + React + Tailwind + Framer Motion
- Backend: FastAPI
- LLM: Ollama (default model `gemma3`)
- Agents: LangGraph planner/research/executor/memory graph
- Memory: ChromaDB vector store
- Persistence: PostgreSQL
- Auth: JWT login endpoint
- Voice: Whisper STT + pyttsx3 TTS

## Project Structure

```text
orchestrix-ai/
├── frontend/
├── backend/
├── docs/
├── README.md
├── .env.example
└── docker-compose.yml
```

## Setup (Windows PowerShell)

### 1) Start dependencies
```powershell
cd orchestrix-ai
docker compose up -d
```

### 2) Backend
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item ..\.env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3) Frontend
```powershell
cd ..\frontend
npm install
$env:NEXT_PUBLIC_API_BASE_URL="http://localhost:8000/api"
npm run dev
```

### 4) Ollama model setup
```powershell
ollama pull gemma3
ollama serve
```

## API Endpoints
- `POST /api/chat` streaming assistant output
- `POST /api/agent/run` run LangGraph workflow
- `GET /api/conversations?user_id=` fetch chat history
- `POST /api/memory/save` save memory to Chroma
- `GET /api/memory/search?user_id=&query=` semantic retrieval
- `POST /api/voice/stt` speech to text (Whisper)
- `POST /api/voice/tts` text to speech (pyttsx3)
- `GET /api/tools` list registered tools
- `POST /api/auth/login` return JWT for user id

## Tooling in MVP
- Calculator
- File reader
- Python execution (restricted builtins)
- Web search placeholder
- Email automation placeholder
- Calendar automation placeholder

## Testing

```powershell
cd backend
pytest
```

## Notes
- If you want Coqui TTS, swap the implementation in `app/services/voice.py`.
- Frontend contains markdown rendering, animated cards, and responsive dashboard layout.
