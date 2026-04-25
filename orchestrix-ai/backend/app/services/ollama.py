import json
from collections.abc import Generator

import httpx

from app.core.config import get_settings

settings = get_settings()


def stream_chat(message: str, system_prompt: str = "You are Orchestrix AI") -> Generator[str, None, None]:
    payload = {
        "model": settings.ollama_model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
        "stream": True,
    }

    with httpx.stream("POST", f"{settings.ollama_base_url}/api/chat", json=payload, timeout=120) as response:
        response.raise_for_status()
        for line in response.iter_lines():
            if not line:
                continue
            data = json.loads(line)
            content = data.get("message", {}).get("content", "")
            if content:
                yield content
