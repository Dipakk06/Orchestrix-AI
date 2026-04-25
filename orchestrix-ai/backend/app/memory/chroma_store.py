from uuid import uuid4

import chromadb

from app.core.config import get_settings

settings = get_settings()


class ChromaMemoryStore:
    def __init__(self) -> None:
        self.client = chromadb.HttpClient(host=settings.chroma_host, port=settings.chroma_port)
        self.collection = self.client.get_or_create_collection(name=settings.chroma_collection)

    def save(self, user_id: str, content: str, importance: int) -> dict:
        memory_id = str(uuid4())
        self.collection.add(
            ids=[memory_id],
            documents=[content],
            metadatas=[{"user_id": user_id, "importance": importance}],
        )
        return {"id": memory_id, "user_id": user_id, "content": content, "importance": importance}

    def search(self, user_id: str, query: str, limit: int = 5) -> list[dict]:
        result = self.collection.query(query_texts=[query], n_results=limit)
        docs = result.get("documents", [[]])[0]
        ids = result.get("ids", [[]])[0]
        meta = result.get("metadatas", [[]])[0]
        filtered = []
        for idx, doc in enumerate(docs):
            metadata = meta[idx] if idx < len(meta) else {}
            if metadata.get("user_id") == user_id:
                filtered.append({"id": ids[idx], "content": doc, "metadata": metadata})
        return filtered
