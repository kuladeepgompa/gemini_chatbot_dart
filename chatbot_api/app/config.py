import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    MODEL_NAME = 'gemini-1.5-flash'
    MAX_TOKENS = 1000
    TEMPERATURE = 0.7
    REQUEST_TIMEOUT = 30
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')