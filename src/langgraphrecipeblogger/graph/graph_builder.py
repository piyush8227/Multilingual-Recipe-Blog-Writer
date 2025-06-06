from langgraph.graph import StateGraph, END
from src.langgraphrecipeblogger.state.recipe_state import RecipeState

# Import each node function
from src.langgraphrecipeblogger.nodes.orchestrator import orchestrator
from src.langgraphrecipeblogger.nodes.recipe_worker import get_recipe_instructions
from src.langgraphrecipeblogger.nodes.ingredient_worker import scale_ingredient
from src.langgraphrecipeblogger.nodes.metadata_extractor import extract_metadata
from src.langgraphrecipeblogger.nodes.blog_generator import generate_blog

def build_graph():
    builder = StateGraph(RecipeState)

    # Add each node
    builder.add_node("orchestrator", orchestrator)
    builder.add_node("recipe_worker", get_recipe_instructions)
    builder.add_node("ingredient_worker", scale_ingredient)
    builder.add_node("extract_metadata", extract_metadata)
    builder.add_node("blog_generator", generate_blog)

    # Define edges (graph structure)
    builder.set_entry_point("orchestrator")
    builder.add_edge("orchestrator", "extract_metadata")
    builder.add_edge("orchestrator", "recipe_worker")
    builder.add_edge("orchestrator", "ingredient_worker")
    builder.add_edge("recipe_worker", "blog_generator")
    builder.add_edge("ingredient_worker", "blog_generator")
    builder.add_edge("extract_metadata", "blog_generator")
    builder.add_edge("blog_generator", END)
    
    return builder.compile()

generate_blog_workflow = build_graph()
