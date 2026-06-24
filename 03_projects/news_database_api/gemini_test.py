from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Summarize: OpenAI released a new AI model."
)

print(response.text)