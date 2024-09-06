# Use a base image with Python
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Command to run your application
CMD ["python", "run_llama.py"]
