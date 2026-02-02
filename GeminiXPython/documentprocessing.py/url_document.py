from google import genai
from google.genai import types
import httpx, pathlib

client = genai.Client()

doc_url = "https://www.orimi.com/pdf-test.pdf"
doc_data = httpx.get(doc_url).content
prompt = "Summarize the document"

filepath = pathlib.Path('report.pdf')
doc_data = filepath.read_bytes()

pdf = types.Part.from_bytes(
    data=doc_data,
    mime_type="application/pdf"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = [pdf, prompt],
    config=types.GenerateContentConfig(
        system_instruction="Answer within 300 words"
        
    )
)
print(response.text)