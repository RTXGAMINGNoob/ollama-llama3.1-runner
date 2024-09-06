import requests

def run_llama_model():
    # Replace '5000' with the actual port number your server is running on
    url = "http://localhost:5000/run-llama"  # Change port as needed

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        result = response.json()  # Assuming the response is JSON
        print("Model output:", result)
    except requests.exceptions.RequestException as e:
        print("Error while calling the model:", e)

if __name__ == "__main__":
    run_llama_model()
