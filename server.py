from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Load the LLaMA 3.1 uncensored model at server startup
# Replace with the actual command to load the model using Ollama
model_loading_command = "ollama run llama3.1-uncensored"

@app.route('/run-llama', methods=['POST'])
def run_llama_model():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Run the model with the user input
        result = subprocess.run(
            [model_loading_command, user_input],
            capture_output=True,
            text=True,
            shell=True
        )

        # Check for errors
        if result.returncode != 0:
            return jsonify({"error": "Model execution failed", "details": result.stderr}), 500
        
        # Return the output from the model
        return jsonify({"output": result.stdout.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
