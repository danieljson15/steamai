from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("STEAM_API_KEY"))