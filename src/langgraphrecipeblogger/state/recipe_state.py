from pydantic import BaseModel, Field
from typing import Optional

class RecipeState(BaseModel):
    recipe_name: str = Field(..., description="Name of the recipe which user wants to make.")
    headcount: int = Field(..., description=(
        "Total number of people who will be served this dish. "
        "Used for scaling ingredient quantities."
    ))

    language: str = Field(
        default="English", description="Language for the generated blog post."
    )

    instructions: Optional[str] = Field(
        default=None, description="Step-by-step cooking instructions."
    )

    ingredients: Optional[str] = Field(
        default=None, description="Scaled ingredient list for the given headcount."
    )

    metadata: Optional[str] = Field(
        default=None, description="Structured metadata about the recipe."
    )

    blog_post: Optional[str] = Field(
        default=None, description="Final recipe blog post (Markdown)."
    )