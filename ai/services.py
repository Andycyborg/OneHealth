
import os
import time

from google import genai
from google.genai import types


def ask_ai(prompt):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return (
            "AI service is not configured. "
            "Please set GEMINI_API_KEY."
        )

    # Try models in this order.
    # If one is temporarily unavailable, try the next one.
    models = [
        "gemini-3.6-flash",
        "gemini-3.5-flash",
        "gemini-3.7-flash",
    ]

    try:

        client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(
                timeout=60000
            )
        )

        last_error = None

        for model in models:

            for attempt in range(2):

                try:

                    print(
                        f"Trying Gemini model: {model} "
                        f"(attempt {attempt + 1})"
                    )

                    response = client.models.generate_content(
                        model=model,
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            temperature=0.4,
                            max_output_tokens=800,
                        ),
                    )

                    if response and response.text:

                        print(
                            f"Gemini success: {model}"
                        )

                        return response.text.strip()

                    last_error = (
                        f"{model} returned an empty response."
                    )

                except Exception as e:

                    last_error = e

                    print(
                        f"Gemini error with {model}: {e}"
                    )

                    # Wait briefly before retrying.
                    time.sleep(2)

        print(
            "All Gemini models failed:",
            last_error
        )

        return (
            "The AI service is temporarily unavailable. "
            "Please try again in a few moments."
        )

    except Exception as e:

        print(
            "Gemini client error:",
            e
        )

        return (
            "Unable to connect to the AI service right now."
        )

