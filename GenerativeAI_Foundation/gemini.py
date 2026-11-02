from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client() # This will use the API key from the .env file

interaction = client.interactions.create(
    model="gemini-3.8-flash", input="what is 2 + 2?"
)

print(interaction)
