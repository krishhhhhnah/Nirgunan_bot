<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# Nirgunan Bot


## Basic Details
### Team Name: Not specified in the codebase


### Team Members
- Team members and colleges: Not specified in the codebase

### Project Description
Nirgunan Bot is a deliberately useless AI chat application. Users submit questions through a browser interface and receive short, absurd, sarcastic, confidently incorrect responses.

The Flask backend sends each question to a locally running Ollama `llama3.2` model and returns the cleaned response to the chat interface.

### The Problem (that doesn't exist)
The project solves the entirely fictional problem of people receiving useful, accurate, and sensible answers from chatbots.

### The Solution (that nobody asked for)
Nirgunan is instructed to avoid correct answers, useful advice, explanations, tutorials, and real calculations. It produces entertaining nonsense instead, limited to one or two sentences and 25 words.

## Technical Details
### Technologies/Components Used
For Software:
- Python
- Flask
- Requests
- HTML, CSS, and vanilla JavaScript
- Ollama with the `llama3.2` model
- Gunicorn

For Hardware:
- No hardware components are used.

### Implementation
For Software:
# Installation

Prerequisites:

- Python 3
- Ollama installed and running
- The Ollama `llama3.2` model

Download the model:

```bash
ollama pull llama3.2
```

Install the Python dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

# Run

Start Ollama, then run the Flask application:

```bash
python app.py
```

Open `http://127.0.0.1:5000` in a browser. The application listens on port 5000 and binds to `0.0.0.0`.

For a WSGI server, the repository also includes Gunicorn:

```bash
gunicorn app:app
```

### Project Documentation
For Software:

# Screenshots

Screenshots are not included in the repository.

# Diagrams

```text
Browser -> Flask GET / -> templates/index.html
Browser -> Flask POST /ask -> Ollama http://localhost:11434/api/generate
Browser <- JSON reply <- Flask <- Ollama
```

The browser submits JSON containing `message`; Flask sends the prompt to Ollama and returns JSON containing `reply`.

For Hardware:

# Schematic & Circuit

Not applicable. This is a software-only project.

# Build Photos

Not applicable. No physical build is used.

### Project Demo
# Video

No demo video is included in the repository.

# Additional Demos

No additional demo materials are included in the repository.

## Team Contributions
- Team contributions are not specified in the codebase.

---
Made with love at TinkerHub Useless Projects

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



