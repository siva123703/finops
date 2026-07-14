import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors as genai_errors

load_dotenv()


class GeminiService:
    """
    Sends prompts to Gemini and returns AI recommendations.
    """

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")
        model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

        print("API Key:", api_key)

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set.")

        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt):
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )
            return getattr(response, "text", "") or ""
        except genai_errors.ClientError as exc:
            status_code = getattr(exc, "code", None)
            message = str(exc).lower()
            if status_code == 429 or "resource_exhausted" in message or "depleted" in message:
                return (
                    "Gemini is temporarily unavailable because the API quota or billing credits "
                    "have been exhausted. Please try again later or update the API configuration."
                )
            raise
