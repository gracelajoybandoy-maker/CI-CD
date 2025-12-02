
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run your Flask API app
CMD ["python", "flask_api.py"]
