from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate

from src.langgraphrecipeblogger.state.recipe_state import RecipeState
from src.langgraphrecipeblogger.utils.llm import llm


def get_recipe_instructions(state: RecipeState) -> Dict[str, Any]:

    """
    Generates a step by step instructions for cooking food.
    """

    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=(
            "You are a recipe-making instructor in a five-star hotel, "
            "an expert in all Indian cuisines."
        )),
        HumanMessage(content=f"Write detailed recipe instructions for {state.recipe_name}.")
    ])

    chain = prompt | llm
    response = chain.invoke({"recipe_name": state.recipe_name})
    return {"instructions": response.content}
