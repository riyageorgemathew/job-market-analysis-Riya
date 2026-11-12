import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("API_ID")
api_key = os.getenv("API_KEY")

if api_id and api_key:
    print("API ID and API KEY loaded successfully.")
else:
    print("Failed to load API ID And API KEY.")