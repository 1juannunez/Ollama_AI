
Make sure to download Download Ollama('https://github.com/ollama/ollama')

Setup Instructions
# Clone repository
git clone [repo]

# Create a virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Ensure Ollama is running
ollama list \n
ollama pull llama3.2 (If you don't have a model, let's download a good one)

# Run the generator
python auto_onenote.py
