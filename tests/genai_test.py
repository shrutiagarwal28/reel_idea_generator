# from fastapi.testclient import TestClient
# from app.main import app
#
# client = TestClient(app)
#
# def test_generate_caption():
#     response = client.post("/generate", json={
#         "theme": "travel",
#         "tone": "funny",
#         "keywords": ["beach", "sunset"]
#     })
#     assert response.status_code == 200
#     assert "caption" in response.json()