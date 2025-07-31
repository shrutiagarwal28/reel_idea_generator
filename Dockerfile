FROM python:3.11-slim

LABEL authors="Shruti"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /app /app

EXPOSE 8000

# Start FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Use the following command to build the Docker image:
# docker build -t reel_idea_generator .
# Use the following command to run the Docker container:
# docker run -d -p 8000:8000 reel_idea_generator .
#Check logs to confirm it’s working:
#docker ps   # find container ID
#docker logs <container_id>