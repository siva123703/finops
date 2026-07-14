import os
import unittest
from unittest.mock import patch

from src.ai.gemini_service import GeminiService


class GeminiServiceTests(unittest.TestCase):
    def setUp(self):
        os.environ["GEMINI_API_KEY"] = "test-key"

    def test_generate_returns_fallback_when_gemini_is_rate_limited(self):
        class FakeClient:
            class Models:
                @staticmethod
                def generate_content(*args, **kwargs):
                    from google.genai.errors import ClientError

                    raise ClientError(
                        429,
                        {
                            "error": {
                                "code": 429,
                                "message": "Your prepayment credits are depleted.",
                                "status": "RESOURCE_EXHAUSTED",
                            }
                        },
                        None,
                    )

            models = Models()

        with patch("src.ai.gemini_service.genai.Client", return_value=FakeClient()):
            service = GeminiService()
            response = service.generate("Say hello in one sentence.")

        self.assertIn("temporarily unavailable", response.lower())
        self.assertIn("gemini", response.lower())


if __name__ == "__main__":
    unittest.main()
