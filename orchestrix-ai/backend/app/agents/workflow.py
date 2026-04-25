from typing import TypedDict

from langgraph.graph import END, StateGraph

from app.tools.registry import TOOLS


class AgentState(TypedDict):
    task: str
    plan: str
    research: str
    execution: str
    memory_note: str


def planner_node(state: AgentState) -> AgentState:
    state["plan"] = f"Plan: Break task '{state['task']}' into executable steps."
    return state


def research_node(state: AgentState) -> AgentState:
    query = state["task"]
    state["research"] = TOOLS["web_search"](query)
    return state


def executor_node(state: AgentState) -> AgentState:
    state["execution"] = f"Executed plan using research: {state['research']}"
    return state


def memory_node(state: AgentState) -> AgentState:
    state["memory_note"] = f"Remember outcome for task: {state['task']}"
    return state


def build_graph():
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node("planner", planner_node)
    graph_builder.add_node("research", research_node)
    graph_builder.add_node("executor", executor_node)
    graph_builder.add_node("memory", memory_node)

    graph_builder.set_entry_point("planner")
    graph_builder.add_edge("planner", "research")
    graph_builder.add_edge("research", "executor")
    graph_builder.add_edge("executor", "memory")
    graph_builder.add_edge("memory", END)

    return graph_builder.compile()


def run_agent(task: str) -> dict:
    app = build_graph()
    initial_state: AgentState = {
        "task": task,
        "plan": "",
        "research": "",
        "execution": "",
        "memory_note": "",
    }
    return app.invoke(initial_state)
