import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# Gemini Configuration
# -------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# -------------------------
# OpenRouter Configuration
# -------------------------
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

DEBUG_MODEL_1 = os.getenv("DEBUG_MODEL_1", "openai/gpt-4o-mini")
DEBUG_MODEL_2 = os.getenv("DEBUG_MODEL_2", "anthropic/claude-3-haiku")

if not OPENROUTER_API_KEY:
    print("WARNING: OPENROUTER_API_KEY not found. Advanced debug may fail.")