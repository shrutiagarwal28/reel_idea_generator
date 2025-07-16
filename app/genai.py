import os
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=key)

def generate_instagram_caption():
    description = input("Enter a wedding video description: ")
    prompt = (
        "Generate 5 creative Instagram captions and 5 relevant hashtags for the following wedding video description. "
        "Each caption should be wedding-focused and emotional. "
        f"Video description: {description}\n\n"
        "Format the response as:\n"
        "CAPTIONS:\n"
        "1. [caption]\n"
        "2. [caption]\n"
        "...\n\n"
        "HASHTAGS:\n"
        "#[hashtag] #[hashtag] #[hashtag] #[hashtag] #[hashtag]"
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    caption = response.text.strip()
    print("Prompt tokens used:", response.usage_metadata.prompt_token_count)
    print("Candidates tokens used:", response.usage_metadata.candidates_token_count, "\n")
    print("Generated Instagram Caption:", caption)

    app_dir = os.path.dirname(__file__)
    caption_file = os.path.join(app_dir, "..", "outputs", "caption.txt")
    with open(caption_file, "a") as f:
        f.write(f"Description: {description}\n"
                f"Caption: {caption}\n\n"
                f"Prompt tokens used: {response.usage_metadata.prompt_token_count}\n")


generate_instagram_caption()