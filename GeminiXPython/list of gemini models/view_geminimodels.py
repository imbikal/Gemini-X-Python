from google import genai

# Pass your API key directly here
client = genai.Client() 

# List all models available to your key
for model in client.models.list():
    print(model.name)