from graph import graph

# Generate Mermaid PNG using LangGraph
graph.get_graph().draw_mermaid_png(output_file_path="screenshots/workflow.png")

print("Workflow diagram saved as workflow.png")