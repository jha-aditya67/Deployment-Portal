# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy the requirements file and install Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our updated application code
COPY app.py .

# Tell Docker that the container will listen on network port 80
EXPOSE 80

CMD ["python", "app.py"]
