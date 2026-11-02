import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("AI_API_KEY")
)  # This will use the API key from the .env file

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role": "system", "content": "You are an expert in maths and only maths related questions."}, 
        {"role": "user", "content": "what is 2 + 2?"}
    ]
)

print(interaction.output_text)
