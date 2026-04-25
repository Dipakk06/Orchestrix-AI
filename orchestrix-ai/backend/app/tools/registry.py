from app.tools.builtin import (
    calculator_tool,
    calendar_automation_placeholder,
    email_automation_placeholder,
    file_reader_tool,
    python_exec_tool,
    web_search_placeholder,
)

TOOLS = {
    "calculator": calculator_tool,
    "file_reader": file_reader_tool,
    "python_exec": python_exec_tool,
    "web_search": web_search_placeholder,
    "email_automation": email_automation_placeholder,
    "calendar_automation": calendar_automation_placeholder,
}


def list_tools() -> list[dict]:
    return [
        {
            "name": name,
            "description": fn.__doc__ or "No description",
        }
        for name, fn in TOOLS.items()
    ]
