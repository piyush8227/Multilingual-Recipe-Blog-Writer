from typing import Dict, Any
from src.langgraphrecipeblogger.state.recipe_state import RecipeState

def orchestrator(state: RecipeState) -> Dict[str, Any]:
    """
    Orchestrates the recipe blog-writing task by passing along
    the recipe_name, headcount, and language to downstream nodes.
    """
    return {
        "recipe_name": state.recipe_name,
        "headcount": state.headcount,
        "language": state.language,
    }
