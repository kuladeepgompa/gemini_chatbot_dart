import google.generativeai as genai
from app.config import Config
from typing import Dict, Any

class GeminiService:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(Config.MODEL_NAME)
        self.generation_config = genai.types.GenerationConfig(
            max_output_tokens=Config.MAX_TOKENS,
            temperature=Config.TEMPERATURE
        )

    def generate_response(self, prompt: str) -> Dict[str, Any]:
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config,
                request_options={'timeout': Config.REQUEST_TIMEOUT}
            )
            return {'response': response.text}
        except Exception as e:
            raise RuntimeError(f"Gemini API error: {str(e)}")
