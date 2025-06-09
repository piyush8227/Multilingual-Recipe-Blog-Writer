from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate
from src.langgraphrecipeblogger.state.recipe_state import RecipeState
from src.langgraphrecipeblogger.utils.llm import llm


def generate_blog(state: RecipeState) -> Dict[str, Any]:
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=(
            "You are an SEO expert and food blogger, "
            "writing engaging, multilingual recipe blogs with a slightly humorous tone. "
            "Format the blog using Markdown so it renders beautifully online."
        )),
        HumanMessage(content=(
            f"Generate a catchy blog post **title** and write a full blog for “{state.recipe_name}”,\n"
            f"serving **{state.headcount}** people, in **{state.language}**.\n"
            "Tone: witty yet informative.\n\n"
            "# 🏷️ Title\n"
            "- Catchy and SEO-optimized (use a top-level `#` heading).\n\n"
            "## 📝 Metadata (bold labels)\n"
            f"{state.metadata}\n\n"
            "## 🧂 Ingredients (bullet list)\n"
            f"{state.ingredients}\n\n"
            "## 🔪 Instructions (numbered list)\n"
            f"{state.instructions}\n\n"
            "## 🎉 Conclusion\n"
            "End with a friendly call to action that encourages readers to try the recipe.\n\n"
            "# 💡 Output Requirements\n"
            "- Use `#`, `##`, and `**` for Markdown formatting.\n"
            "- Section headers must be larger and bold. Do not explain what you are doing—just produce the blog."
        ))
    ])

    chain = prompt | llm
    response = chain.invoke({
        "recipe_name": state.recipe_name,
        "language": state.language,
        "headcount": state.headcount,
        "metadata": state.metadata,
        "ingredients": state.ingredients,
        "instructions": state.instructions
    })
    
    blog_post = response.content

    new_entry = {
        "role": "user",
        "content": f"Generate blog for {state.recipe_name} in {state.language}"
    }
    new_response = {
        "role": "assistant",
        "content": blog_post
    }

    # Append to existing history
    updated_history = state.chat_history + [new_entry, new_response]

    return {"blog_post": response.content, "chat_history": updated_history}
