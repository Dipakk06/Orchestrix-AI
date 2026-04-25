from pydantic import BaseModel


class MemorySaveRequest(BaseModel):
    user_id: str
    content: str
    importance: int = 5


class MemorySearchRequest(BaseModel):
    user_id: str
    query: str
    limit: int = 5
