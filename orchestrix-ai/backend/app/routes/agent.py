from fastapi import APIRouter

from app.agents.workflow import run_agent
from app.schemas.chat import AgentRunRequest

router = APIRouter(tags=["agent"])


@router.post("/agent/run")
def run(payload: AgentRunRequest):
    result = run_agent(payload.task)
    return {"status": "ok", "result": result}
