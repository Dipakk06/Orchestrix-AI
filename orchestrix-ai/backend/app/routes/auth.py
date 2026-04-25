from fastapi import APIRouter
from pydantic import BaseModel

from app.auth.jwt import create_access_token

router = APIRouter(tags=["auth"])


class LoginRequest(BaseModel):
    user_id: str


@router.post("/auth/login")
def login(payload: LoginRequest):
    return {"access_token": create_access_token(payload.user_id), "token_type": "bearer"}
