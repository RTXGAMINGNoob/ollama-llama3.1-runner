# llama3.1-uncensored.py

import requests
import sys

def run_llama_model(input_text):
    # URL to Ollama API for running the model
    url = "http://localhost:11434/run-llama"  # Replace with actual Ollama API endpoint if different

    # Send POST request with input text
    response = requests.post(url, json={"input": input_text})

    if response.status_code == 200:
        return response.json().get("output", "No output returned")
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    input_text = sys.argv[1] if len(sys.argv) > 1 else "Default input"
    output = run_llama_model(input_text)
    print(output)
