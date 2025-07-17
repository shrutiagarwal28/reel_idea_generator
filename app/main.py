from fastapi import FastAPI
from pydantic import BaseModel
from app.genai import generate_instagram_caption

app = FastAPI()

class CaptionRequest(BaseModel):
    description: str
    number_of_captions: int = 5

@app.post("/generate-caption/")
def get_caption(req: CaptionRequest):
    """
    API endpoint to generate Instagram captions based on a wedding video description.
    """
    result = generate_instagram_caption(req.description)
    return result
