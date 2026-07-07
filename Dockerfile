FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ src/
COPY models/ models/

# Copy MLflow artifacts if they exist
COPY mlruns/ mlruns/

# Expose ports
EXPOSE 8000
EXPOSE 5000

# Command
CMD ["uvicorn", "src.predict:app", "--host", "0.0.0.0", "--port", "8000"]
