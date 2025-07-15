from google import genai

client = genai.Client(api_key="AIzaSyAEdslrHcs3XmTzJIdBSQ8Ba4lyEdhAC_g")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me about the latest trends in wedding photography"
)

print(response.text)