from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

# Define your desired data structure.
class CookingStats(BaseModel):
    preparationTimeInMinutes: int = Field(description="estimated preparation time in minutes")
    cookingTimeInMinutes: int = Field(description="estimated cooking time in minutes without preparation time")
    calories: int = Field(description="how many calories")

cooking_stats_parser = JsonOutputParser(pydantic_object=CookingStats)