import argparse
import os
import sys
import json

# Attempt to import the OpenAI SDK; instruct installation if missing
try:
    from openai import OpenAI
    
    client = OpenAI(api_key=api_key)  # Import the OpenAI Python client
except ImportError:
    print("Error: The 'openai' package is required but not installed.")
    print("Install it by running: pip install openai")
    sys.exit(1)  # Exit if OpenAI is not installed


def generate_reel_ideas(count: int, theme: str):
    """
    Calls the OpenAI API to generate Instagram reel ideas for a given wedding theme.
    Prints a nicely formatted list of titles, captions, and hashtags.
    """
    # Ensure your API key is set in the environment
    api_key = os.getenv("OPENAI_API_KEY")  # Get the API key from environment variable
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        sys.exit(1)  # Exit if API key is missing
      # Set the API key for OpenAI

    prompt = (
        f"Generate {count} Instagram reel ideas for {theme} weddings. "
        "For each idea, provide:\n"
        "- title (short headline)\n"
        "- caption (1-2 sentences)\n"
        "- hashtags (list of trending wedding-related hashtags)\n"
        "Respond in valid JSON format as a list of objects with keys 'title', 'caption', and 'hashtags'."
    )

    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=500)
    except Exception as e:
        print(f"API request failed: {e}")
        sys.exit(1)

    content = response.choices[0].message.content
    try:
        ideas = json.loads(content)
    except json.JSONDecodeError:
        print("Failed to parse JSON from API response:")
        print(content)
        sys.exit(1)

    for idx, idea in enumerate(ideas, start=1):
        title = idea.get("title", "[No title]")
        caption = idea.get("caption", "[No caption]")
        hashtags = idea.get("hashtags", [])
        print(f"Idea {idx}: {title}\nCaption: {caption}\nHashtags: {' '.join(hashtags)}\n{'-'*40}")


def main():
    parser = argparse.ArgumentParser(
        description="AI-Powered Instagram Reel Idea Generator for wedding themes"
    )
    parser.add_argument(
        "-n", "--number", type=int, default=5,
        help="Number of reel ideas to generate (default: 5)"
    )
    parser.add_argument(
        "-t", "--theme", type=str, default="Indian wedding",
        help="Wedding theme or niche to tailor ideas to (default: 'Indian wedding')"
    )
    parser.add_argument(
        "--test", action='store_true', help="Run unit tests instead of generating ideas"
    )
    args = parser.parse_args()

    if args.test:
        # Run tests and exit
        import unittest

        class TestJSONParsing(unittest.TestCase):
            def test_parse_valid_json(self):
                content = '[{"title":"Test","caption":"Test caption","hashtags":["#a","#b"]}]'
                ideas = json.loads(content)
                self.assertEqual(len(ideas), 1)
                self.assertEqual(ideas[0]['title'], 'Test')
                self.assertEqual(ideas[0]['caption'], 'Test caption')
                self.assertEqual(ideas[0]['hashtags'], ['#a', '#b'])

        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestJSONParsing)
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        sys.exit(0 if result.wasSuccessful() else 1)
    else:
        generate_reel_ideas(args.number, args.theme)


if __name__ == "__main__":
    main()
