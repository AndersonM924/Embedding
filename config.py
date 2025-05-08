from dotenv import load_dotenv
import os

load_dotenv()  # Lee el .env en el proyecto

# Gemini Embeddings
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
