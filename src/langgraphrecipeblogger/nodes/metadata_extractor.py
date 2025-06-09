from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate

from src.langgraphrecipeblogger.state.recipe_state import RecipeState
from src.langgraphrecipeblogger.utils.llm import llm


def extract_metadata(state: RecipeState) -> Dict[str, Any]:

    """
    This agent extracts the metadata from the recipe to help filter out recipes and gives a short dietry info.
    """
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are an expert recipe metadata extractor."),
        HumanMessage(content=(
            f"Extract the following metadata for the recipe: {state.recipe_name}.\n\n"
            "Return in this exact format:\n"
            "Cuisine: ...\n"
            "Cooking Time: ...\n"
            "Difficulty: ...\n"
            "Dietary Info: ...\n"
            "Calories per Serving: ...\n"
            "Tools Needed: ..."
        ))
    ])

    chain = prompt | llm
    response = chain.invoke({"recipe_name": state.recipe_name})
    return {"metadata": response.content}
