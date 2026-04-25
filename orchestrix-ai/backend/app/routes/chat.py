import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.conversation import Conversation
from app.schemas.chat import ChatRequest, ConversationOut
from app.services.ollama import stream_chat

router = APIRouter(tags=["chat"])
logger = logging.getLogger(__name__)


@router.post("/chat")
def chat(payload: ChatRequest, db: Session = Depends(get_db)):
    try:
        db.add(Conversation(user_id=payload.user_id, role="user", content=payload.message, title="Chat"))
        db.commit()

        def event_stream():
            assistant_content = []
            for token in stream_chat(payload.message):
                assistant_content.append(token)
                yield token

            db.add(
                Conversation(
                    user_id=payload.user_id,
                    role="assistant",
                    content="".join(assistant_content),
                    title="Chat",
                )
            )
            db.commit()

        return StreamingResponse(event_stream(), media_type="text/plain")
    except Exception as exc:  # noqa: BLE001
        logger.exception("Chat request failed")
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get("/conversations", response_model=list[ConversationOut])
def conversations(user_id: str, db: Session = Depends(get_db)):
    return db.query(Conversation).filter(Conversation.user_id == user_id).order_by(Conversation.created_at.asc()).all()
