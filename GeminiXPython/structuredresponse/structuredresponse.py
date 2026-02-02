
from google import genai
from pydantic import BaseModel
import enum

class Grade(enum.Enum):  # Ratings to the recipies
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    
      
class Recipie(BaseModel):         # Parent class as Basemodels and fields below
    recipe_name :str
    ingridents_name : list[str]

client = genai.Client()

prompt = "List few popular chicken recipies and include amount of ingridents to prepare it"

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents = prompt,
    config = {
        "response_mime_type" : "application/json",
        "response_schema": list[Recipie]
    }
)

print(response.text)
 

"""
Part 1: Imports
from google import genai Imports the Google GenAI SDK, which allows your Python script to communicate with Google's servers.

from pydantic import BaseModel Imports Pydantic, a library used for data validation. It ensures the AI gives you exactly the data types (strings, lists, etc.) you asked for.

Part 2: Defining the Structure
class Recipie(BaseModel): You are creating a new class called Recipie. By inheriting from BaseModel, you are telling the AI: "Any 'Recipe' you create must follow the rules I am about to list."

recipe_name : str Defines a field that must be a string. This will be the title of the dish.

ingridents_name : list[str] Defines a field that must be a list of strings. This is where the AI will put the list of ingredients.

Part 3: Setup and Prompt
client = genai.Client() This initializes the connection. It’s like picking up the phone to call the Gemini model.

prompt = "List few popular chicken recipies..." This is your "Human" instruction. You are telling the AI what content you want it to look for.

Part 4: The Execution (The most important part)
response = client.models.generate_content(...) This sends your request to the gemini-2.0-flash model.

"response_mime_type" : "application/json" This is a strict instruction: "Do not talk to me. Do not say 'Here are some recipes.' Only return raw JSON code."

"response_schema": list[Recipie] This tells the model to take the prompt results and "pour" them into your Pydantic mold. Because it's list[Recipie], the model knows it can return multiple recipes in an array.

Part 5: The Output
print(response.text) This prints the final result. Because of the settings above, this won't look like a chat; it will look like a block of code that a database or another program can read instantly.
"""
