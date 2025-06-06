from IPython.display import display, Image
from langgraph.graph import END
from langgraphrecipeblogger.state.recipe_state import RecipeState
from langgraphrecipeblogger.graph.graph_builder import build_graph

def run_example():
    # Compile the graph once
    graph = build_graph()

    # Sample input (you can replace these values or load from a JSON file)
    user_input = {
        "recipe_name": "Chicken Biryani",
        "headcount": 2,
    }

    # Invoke the graph
    result = graph.invoke(user_input)

    print("\n📝 Final Blog Post:\n")
    print(result["blog_post"])
    
if __name__ == "__main__":
    run_example()
