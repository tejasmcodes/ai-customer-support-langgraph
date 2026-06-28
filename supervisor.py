from llm import llm
def supervisor_agent(state):
    prompt = f"""
You are the Human Supervisor of a customer support system.

Your job is to approve and improve the response before it is sent to the customer.

DO NOT explain your changes.
DO NOT critique the response.
DO NOT provide suggestions.
DO NOT mention that you improved it.

Simply return the final customer-facing response.

Start with:

Human Supervisor Approved.

Then provide the improved response.

Customer Response:
{state["response"]}
"""

    response = llm.invoke(prompt)

    state["approved"] = True
    state["response"] = response.content

    return state