FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

ENV PYTHONUNBUFFERED=1

# Run mcp_pipe with calculator.py by default
CMD ["python", "mcp_pipe.py", "calculator.py"]
