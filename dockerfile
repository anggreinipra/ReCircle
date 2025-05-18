# Base image
FROM python:3.11-slim-bullseye

# Working directory
WORKDIR /app

# Install pip & uv
RUN apt-get update && apt-get upgrade -y && apt-get install -y gcc && apt-get clean
RUN pip install --upgrade pip uv

# Copy dependencies
COPY requirements.txt .

# Install deps
RUN uv pip install --system --requirement requirements.txt

# Copy all project files
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the app via Python directly (safe & stable)
# CMD ["python", "main.py"]
CMD ["uv", "main:create_app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
