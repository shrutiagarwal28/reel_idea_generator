from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import caption_gen

app = FastAPI(
    title="Instagram Wedding Caption Generator",
    description="Generate creative Instagram captions and hashtags for wedding reels",
    version="1.0"
)

@app.get("/")
def redirct_to_docs():
    return RedirectResponse(url="/docs")
app.include_router(caption_gen.router, prefix="/weddings", tags=["Instagram Captions"])
