from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.database import Base, engine
from app.core.logging import configure_logging
from app.routes import agent, auth, chat, memory, tools, voice

settings = get_settings()
configure_logging()

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix=settings.api_prefix)
app.include_router(chat.router, prefix=settings.api_prefix)
app.include_router(agent.router, prefix=settings.api_prefix)
app.include_router(memory.router, prefix=settings.api_prefix)
app.include_router(voice.router, prefix=settings.api_prefix)
app.include_router(tools.router, prefix=settings.api_prefix)


@app.get("/")
def health():
    return {"status": "ok", "service": settings.app_name}
