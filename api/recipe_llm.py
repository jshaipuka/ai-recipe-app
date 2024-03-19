from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from output_parsers.bullet_point_output_parser import BulletPointOutputParser
from output_parsers.cooking_stats_output_parser import cooking_stats_parser
from langchain_core.output_parsers import StrOutputParser

llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="gpt-35-turbo",
)

def get_recipe(user_input):
    recipe_name = get_recipe_name(user_input)
    recipe_steps = get_recipe_steps(user_input)
    recipe_ingredients = get_recipe_ingredients(recipe_steps)
    recipe_stats = get_recipe_stats(recipe_steps, recipe_ingredients)
    print(recipe_stats)
    recipe = {
        'name': recipe_name,
        'steps': recipe_steps,
        'ingredients': recipe_ingredients,
        'preparationTime': recipe_stats['preparationTimeInMinutes'],
        'cookingTime': recipe_stats['cookingTimeInMinutes'],
        'calories': recipe_stats['calories']
    }
    return recipe

def get_recipe_name(user_input):
    name_prompt = ChatPromptTemplate.from_template(("Name a cooking recipe the user wants: '{user_input}'. The output should be in a two word name."))

    name = name_prompt | llm | StrOutputParser()

    return name.invoke({"user_input": user_input})

def get_recipe_steps(user_input):
    smaller_tasks_prompt = ChatPromptTemplate.from_template(("Break down into a bullet point (bullet point is '*') list of instructions required to prepare the following recipe: {user_input}"))

    break_down_into_smaller_tasks = smaller_tasks_prompt | llm | BulletPointOutputParser()

    return break_down_into_smaller_tasks.invoke({"user_input": user_input})

def get_recipe_ingredients(recipe_steps):
    ingredients_prompt = ChatPromptTemplate.from_template(("Extract into a bullet point (bullet point is '*') list of ingredients for recipe steps: {recipe_steps}. Return only ingredients."))
    
    list_all_ingredients = ingredients_prompt | llm | BulletPointOutputParser()
    
    return list_all_ingredients.invoke({"recipe_steps": recipe_steps})

def get_recipe_stats(recipe_steps, recipe_ingredients):
    stats_prompt = PromptTemplate(
        template="Analyze and provide statistics for user recipe instructions and ingredient list.\n{format_instructions}\n{recipe_steps}\n{recipe_ingredients}",
        input_variables=["recipe_steps", "recipe_ingredients"],
        partial_variables={"format_instructions": cooking_stats_parser.get_format_instructions()},
    )
    
    stats = stats_prompt | llm | cooking_stats_parser

    return stats.invoke({"recipe_steps": recipe_steps, "recipe_ingredients": recipe_ingredients})