from typing import TypedDict, List


class SupportState(TypedDict):
    customer_name: str
    query: str
    intent: str
    department: str
    retrieved_context: str
    memory: List[str]
    requires_approval: bool
    approved: bool
    response: str