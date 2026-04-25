from fastapi import APIRouter

from app.memory.chroma_store import ChromaMemoryStore
from app.schemas.memory import MemorySaveRequest

router = APIRouter(tags=["memory"])
store = ChromaMemoryStore()


@router.post("/memory/save")
def save(payload: MemorySaveRequest):
    saved = store.save(payload.user_id, payload.content, payload.importance)
    return {"status": "saved", "memory": saved}


@router.get("/memory/search")
def search(user_id: str, query: str, limit: int = 5):
    records = store.search(user_id=user_id, query=query, limit=limit)
    return {"count": len(records), "items": records}
