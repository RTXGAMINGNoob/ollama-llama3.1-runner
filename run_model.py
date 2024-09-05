import os
import requests

# Example function to run the Llama model
def run_llama_model():
    # Define your model execution logic here, e.g., using Ollama
    result = requests.get("http://localhost:port/run-llama")
    print(result.json())

if __name__ == "__main__":
    run_llama_model()
