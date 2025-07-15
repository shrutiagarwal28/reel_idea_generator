import time
import random
import google.generativeai as genai  # Import Gemini SDK

# Set your Gemini API key
GENAI_API_KEY = "YOUR_GEMINI_API_KEY"  # Replace with your actual key

genai.configure(api_key=GENAI_API_KEY)

def safe_gemini_chat(prompt, model="gemini-pro", temperature=0.8, max_tokens=100):
    """
    Calls Gemini's chat completion API with basic exponential backoff for rate limits.
    Args:
        prompt (str): The user prompt to send to Gemini.
        model (str): Gemini model name.
        temperature (float): Sampling temperature.
        max_tokens (int): Maximum tokens in response.
    Returns:
        str: Gemini's response text.
    """
    backoff = 1
    for _ in range(5):
        try:
            response = genai.generate_text(
                model=model,
                prompt=prompt,
                temperature=temperature,
                max_output_tokens=max_tokens
            )
            wait = backoff + random.uniform(0, 0.5)
            print(f"Rate limit hit, retrying in {wait:.1f}s…")
            time.sleep(backoff)
            backoff *= 2
    raise RateLimitError("Exceeded rate limit after multiple retries")

# usage:
response = safe_chat_completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content": "say hello"}],
    temperature=0.8,
    max_tokens=100
)
