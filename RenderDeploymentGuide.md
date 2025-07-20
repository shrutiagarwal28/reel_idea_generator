## 🔧 1. Prepare Your App for Deployment
✅ Create a requirements.txt (if not already):
bash
Copy
Edit
pip freeze > requirements.txt
✅ Add a start command in a Procfile (Render uses this):
Create a file named Procfile (no extension) in the root:

less
Copy
Edit
web: uvicorn app.main:app --host=0.0.0.0 --port=10000
This tells Render how to start your FastAPI server.

## 🔐 2. Push Your Code to GitHub
Make sure:

Your .env is NOT committed (should be in .gitignore)

Your code is committed to a GitHub repository

## ☁️ 3. Create a Web Service on Render
Go to https://render.com

Sign up (or log in) and click "New → Web Service"

Connect your GitHub and choose your repo

Set runtime to Python 3.10+

In "Build Command", set:

nginx
Copy
Edit
pip install -r requirements.txt
In "Start Command", set:

nginx
Copy
Edit
uvicorn app.main:app --host=0.0.0.0 --port=10000
## 🔐 4. Set Your GenAI API Key as an Environment Variable
In Render, go to your service’s "Environment" tab

Add key-value pair:

ini
Copy
Edit
GENAI_API_KEY=your_actual_api_key_here
✅ 5. Done! Your app will be hosted at:
arduino
Copy
Edit
https://your-app-name.onrender.com
You can test it by going to:

arduino
Copy
Edit
https://your-app-name.onrender.com/docs
(Since FastAPI auto-generates Swagger docs)

## Redirect to /docs (Swagger UI)
If you prefer users to land on the Swagger UI directly:

python
Copy
Edit
from fastapi.responses import RedirectResponse

@app.get("/")
def redirect_to_docs():
return RedirectResponse(url="/docs")

