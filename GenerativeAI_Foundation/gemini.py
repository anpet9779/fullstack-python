from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key="")

interaction = client.interactions.create(
    model="gemini-3.8-flash", input="what is 2 + 2?"
)

print(interaction)
