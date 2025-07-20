# 🌐 Goal: Convert Your Project into a Web-Accessible API with CI/CD

---

## ✅ 1. Turn Your Script into an API using FastAPI

Wrap your GenAI logic into a web server:

### Example: `main.py` using FastAPI

```python
from fastapi import FastAPI, Request
from pydantic import BaseModel
from genai_logic import generate_captions  # your existing logic

app = FastAPI()

class CaptionRequest(BaseModel):
    theme: str
    tone: str
    keywords: list[str]

@app.post("/generate-captions")
async def get_captions(data: CaptionRequest):
    return {"captions": generate_captions(data.theme, data.tone, data.keywords)}
```

➡️ Run the server with:

```bash
uvicorn main:app --reload
```

---

## ✅ 2. Organize Your Project Structure

Recommended folder layout:

```
genai_caption_gen/
├── app/
│   ├── main.py          # FastAPI app
│   ├── genai_logic.py   # Your GenAI logic
│   └── models.py        # Pydantic schemas
├── tests/
│   └── test_main.py     # Unit tests
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── python-ci.yml  # CI workflow
```

---

## ✅ 3. Deploy the API (Free Options)

Pick a hosting platform:
- [Render](https://render.com): Easiest for FastAPI (recommended)
- [Railway](https://railway.app) or [Fly.io](https://fly.io): Also great for backend APIs
- [Heroku](https://heroku.com): Good if you want a free-tier database (like Postgres)
- For full-stack: Use Vercel (frontend) + Render (API backend)

### Render Setup:
1. Push your code to GitHub
2. Go to [Render](https://render.com), click **"New Web Service"**
3. Link your GitHub repo
4. Set start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

5. Add environment variables like `GENAI_API_KEY` if needed

---

## ✅ 4. Set Up CI with GitHub Actions

Create `.github/workflows/python-ci.yml`:

```yaml
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
```

---

## ✅ 5. Secure Your API

- Use `.env` files or platform secrets (e.g., Render’s environment tab)
- Add rate limiting using libraries like `slowapi`
- Optional: Add API key authentication for public usage

---

## ✅ 6. Add Documentation

- FastAPI automatically provides Swagger UI at `/docs`
- Add usage examples in your `README.md`

---

## ✅ 7. Optional Add-ons to Showcase Skills

- 🧪 Unit + integration tests
- 📦 Dockerize the app for portability
- 📄 Add OpenAPI schema export via FastAPI
- 🌐 Build a React or Streamlit frontend that calls `/generate-captions`
