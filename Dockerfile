# Use the official Ubuntu 20.04 base image
FROM ubuntu:20.04

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && apt-get clean

# Copy requirements.txt into the image
COPY requirements.txt .

# Install Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Command to run your application
CMD ["python3", "server.py"]  # Ensure this points to your main script

EXPOSE 5000
