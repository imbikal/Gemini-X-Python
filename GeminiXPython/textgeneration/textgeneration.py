
from google import genai
from google.genai import types
from PIL import Image


client = genai.Client()               

prompt = input("Enter your prompt : ")

response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = prompt,
    config = types.GenerateContentConfig(
        system_instruction = "Your response should be within 50 words",
        temperature = 0.7     
    )
)

print("The response is")
print("|")
print("|")
print(response.text)
