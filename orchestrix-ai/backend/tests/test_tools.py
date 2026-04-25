from app.tools.builtin import calculator_tool, python_exec_tool


def test_calculator_tool():
    assert calculator_tool("2+2") == "4"


def test_python_exec_tool():
    code = "result = sum(range(5))"
    assert python_exec_tool(code) == "10"
