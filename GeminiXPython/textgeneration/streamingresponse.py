
from google import genai
from google.genai import types
from PIL import Image


client = genai.Client()               

image = Image.open("textgeneration/images/clothes.jpeg")
response = client.models.generate_content_stream(
    model = 'gemini-2.5-flash',
    contents = [image, "Tell me something about this image"],
    config = types.GenerateContentConfig(
        system_instruction = "Your response should be within 500 words, a bit informative",
        temperature = 0.7     
    )
)

for chunk in response:
    print(chunk.text, end="---\n---")

# print("The response is")
# print("|")
# print("|")
# print(response.text)
