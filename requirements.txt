# Base image
FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    curl \
    git

# Install Ollama (Add your specific instructions here)
RUN curl -fsSL https://ollama.ai/install.sh | bash

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the model script
COPY run_model.py .

# Command to run the model
CMD ["python3", "run_model.py"]
