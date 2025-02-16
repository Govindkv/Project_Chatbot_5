import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    print("API Key Loaded Successfully!")
else:
    print("Error: GOOGLE_API_KEY is missing. Check your .env file.")