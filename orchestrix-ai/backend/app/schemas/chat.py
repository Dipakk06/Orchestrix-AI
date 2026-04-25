from typing import Optional

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    user_id: str
    message: str = Field(min_length=1)
    conversation_id: Optional[str] = None


class AgentRunRequest(BaseModel):
    user_id: str
    task: str


class ConversationOut(BaseModel):
    id: int
    user_id: str
    role: str
    content: str
    title: str

    class Config:
        from_attributes = True
