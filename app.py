from graph import graph
from memory import save_query
query = input("Enter Customer Query: ")

state = {
    "customer_name": "",
    "query": query,
    "intent": "",
    "department": "",
    "retrieved_context": "",
    "memory": [],
    "requires_approval": False,
    "approved": False,
    "response": "",
}
save_query(query)
result = graph.invoke(state)

print("=" * 50)
print("Customer Query:", query)
print("Detected Intent:", result["intent"])

if result["intent"] == "Memory":
    print("Route: Memory Agent")
elif result["intent"] == "Sales":
    print("Route: Sales Agent")
elif result["intent"] == "Technical":
    print("Route: Technical Support Agent")
elif result["intent"] == "Billing":
    if result["requires_approval"]:
        print("Route: Billing Agent → Supervisor Agent")
    else:
        print("Route: Billing Agent")
elif result["intent"] == "Account":
    print("Route: Account Agent")

print("\nFinal Response:\n")
print(result["response"])
print("=" * 50)