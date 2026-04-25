from fastapi import APIRouter

from app.tools.registry import list_tools

router = APIRouter(tags=["tools"])


@router.get("/tools")
def tools():
    return {"tools": list_tools()}
