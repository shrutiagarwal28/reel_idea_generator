from fastapi import APIRouter
from pydantic import BaseModel
from app.genai import generate_instagram_caption

router = APIRouter()

class CaptionRequest(BaseModel):
    description: str
    number_of_captions: int = 5

@router.post("/generate-caption/")
def get_caption(request: CaptionRequest):
    """
    API endpoint to generate Instagram captions based on a wedding video description.
    """
    result = generate_instagram_caption(request.description)
    return {result}
