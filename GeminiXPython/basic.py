import os
from google import genai

client = genai.Client(                 # The way to access the gemini key from env
    api_key=os.getenv("GEMINI_API_KEY")
)


"""
No need to pass like this :

client = genai.Client(api_key="YOUR_API_KEY")

"""

"""
Even easier way:

client = genai.Client()      # Just this much is enough to access the key

"""


prompt = input("Enter your prompt : ")

response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = prompt
)

print("The response is")
print("|")
print("|")
print(response.text)