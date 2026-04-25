from pathlib import Path


def calculator_tool(expression: str) -> str:
    """Evaluate a safe math expression."""
    allowed = set("0123456789+-*/(). %")
    if not set(expression).issubset(allowed):
        return "Invalid characters in expression"
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as exc:  # noqa: BLE001
        return f"Calculator error: {exc}"


def file_reader_tool(file_path: str) -> str:
    """Read UTF-8 text from a file path."""
    path = Path(file_path)
    if not path.exists():
        return "File not found"
    if path.is_dir():
        return "Path is a directory"
    return path.read_text(encoding="utf-8")[:4000]


def python_exec_tool(code: str) -> str:
    """Run restricted python code and return `result` variable."""
    local_vars: dict = {}
    safe_builtins = {"len": len, "sum": sum, "min": min, "max": max, "range": range}
    try:
        exec(code, {"__builtins__": safe_builtins}, local_vars)
        return str(local_vars.get("result", "Executed. Set `result` variable for output."))
    except Exception as exc:  # noqa: BLE001
        return f"Execution error: {exc}"


def web_search_placeholder(query: str) -> str:
    """Placeholder web search tool."""
    return f"[placeholder] web_search results for: {query}"


def email_automation_placeholder(payload: str) -> str:
    """Placeholder email automation tool."""
    return f"[placeholder] email automation called with: {payload}"


def calendar_automation_placeholder(payload: str) -> str:
    """Placeholder calendar automation tool."""
    return f"[placeholder] calendar automation called with: {payload}"
