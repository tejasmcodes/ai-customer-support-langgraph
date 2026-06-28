from rag import retrieve_context
from llm import llm
from memory import get_previous_query

def classify_intent(state):
    query = state["query"].lower()

    if any(word in query for word in [
        "previous issue",
        "previous query",
        "last issue",
        "last query",
        "conversation history",
        "what was my previous",
        "remember",
        "earlier"
    ]):
        state["intent"] = "Memory"
        state["department"] = "Memory"
        return state
    
    # Billing
    if any(word in query for word in [
        "refund", "invoice", "payment", "billing", "charge"
    ]):
        state["intent"] = "Billing"
        state["department"] = "Billing"
        return state

    # Account
    if any(word in query for word in [
        "password", "login", "profile", "account", "activate", "deactivate"
    ]):
        state["intent"] = "Account"
        state["department"] = "Account"
        return state

    # Sales
    if any(word in query for word in [
        "price", "pricing", "plan", "subscription", "cost"
    ]):
        state["intent"] = "Sales"
        state["department"] = "Sales"
        return state

    # Technical
    if any(word in query for word in [
        "error", "crash", "bug", "install", "configuration", "upload", "issue"
    ]):
        state["intent"] = "Technical"
        state["department"] = "Technical"
        return state

    

    # Fallback to LLM
    prompt = f"""
    Classify the customer query into exactly one of these:

    Sales
    Technical
    Billing
    Account

    Return ONLY the category.

    Customer Query:
    {state['query']}
"""

    response = llm.invoke(prompt)

    state["intent"] = response.content.strip()
    state["department"] = state["intent"]

    return state


def sales_agent(state):
    context = retrieve_context("Sales")

    prompt = f"""
You are a Sales Support Assistant.

Use ONLY the information below to answer.

Context:
{context}

Customer Query:
{state['query']}
"""

    response = llm.invoke(prompt)

    state["retrieved_context"] = context
    state["response"] = response.content

    return state


def technical_agent(state):
    context = retrieve_context("Technical")

    prompt = f"""
You are a Technical Support Assistant.

Use ONLY the information below.

Context:
{context}

Customer Query:
{state['query']}
"""

    response = llm.invoke(prompt)

    state["retrieved_context"] = context
    state["response"] = response.content

    return state


def billing_agent(state):
    context = retrieve_context("Billing")

    prompt = f"""
        You are a Billing Support Assistant.

        Use ONLY the information below.

        Context:
        {context}

        Customer Query:
        {state['query']}
        """

    response = llm.invoke(prompt)

    state["retrieved_context"] = context
    state["response"] = response.content

    query = state["query"].lower()

    approval_keywords = [
        "refund",
        "cancel",
        "subscription cancellation",
        "account closure",
        "close account",
        "compensation",
        "management",
    ]

    state["requires_approval"] = any(
        word in query for word in approval_keywords
    )

    return state


def account_agent(state):
    context = retrieve_context("Account")

    prompt = f"""
You are an Account Support Assistant.

Use ONLY the information below.

Context:
{context}

Customer Query:
{state['query']}
"""

    response = llm.invoke(prompt)

    state["retrieved_context"] = context
    state["response"] = response.content

    return state


def memory_agent(state):
    previous = get_previous_query()

    state["response"] = f"Your previous issue was:\n\n{previous}"

    return state

