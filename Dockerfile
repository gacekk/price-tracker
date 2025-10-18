FROM python:3.11-slim

WORKDIR /app
COPY amazon_tracker.py .
RUN pip install beautifulsoup4 requests

CMD ["python", "amazon_tracker.py"]
