from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate

from src.langgraphrecipeblogger.state.recipe_state import RecipeState
from src.langgraphrecipeblogger.utils.llm import llm


def scale_ingredient(state: RecipeState) -> Dict[str, Any]:
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=(
            "You are a cooking assistant. You also help to scale ingredients "
            "according to provided headcount."
        )),
        HumanMessage(content=(
            f"List ingredients and scale them to serve {state.headcount} people for {state.recipe_name}. "
            "Avoid adding code blocks or visible calculations; perform all calculations backstage."
        ))
    ])

    chain = prompt | llm
    response = chain.invoke({
        "recipe_name": state.recipe_name,
        "headcount": state.headcount
    })
    return {"ingredients": response.content}
