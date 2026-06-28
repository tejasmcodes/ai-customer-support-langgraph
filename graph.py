from langgraph.graph import StateGraph, END

from state import SupportState
from supervisor import supervisor_agent
from agents import (
    classify_intent,
    sales_agent,
    technical_agent,
    billing_agent,
    account_agent,
    memory_agent,
)


builder = StateGraph(SupportState)


builder.add_node("IntentClassifier", classify_intent)
builder.add_node("Sales", sales_agent)
builder.add_node("Technical", technical_agent)
builder.add_node("Billing", billing_agent)
builder.add_node("Account", account_agent)
builder.add_node("Memory", memory_agent)
builder.add_node("Supervisor", supervisor_agent)


builder.set_entry_point("IntentClassifier")


def route(state):
    return state["intent"]

def billing_route(state):
    if state["requires_approval"]:
        return "Supervisor"
    return END


builder.add_conditional_edges(
    "IntentClassifier",
    route,
    {
        "Sales": "Sales",
        "Technical": "Technical",
        "Billing": "Billing",
        "Account": "Account",
        "Memory": "Memory",
    },
)


builder.add_edge("Sales", END)
builder.add_edge("Technical", END)
builder.add_conditional_edges(
    "Billing",
    billing_route,
    {
        "Supervisor": "Supervisor",
        END: END,
    }
)
builder.add_edge("Account", END)
builder.add_edge("Memory", END)
builder.add_edge("Supervisor", END)


graph = builder.compile()