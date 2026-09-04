from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/assets/<path:filename>")
def serve_assets(filename):
    assets_dir = os.path.join(app.root_path, "assets")
    return send_from_directory(assets_dir, filename)


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json() or {}

    user_message = data.get("message", "")
    mode = data.get("mode", "USELESS")

    if not user_message:
        return jsonify({
            "response": "You asked absolutely nothing. Impressive."
        })

    system_prompt = f"""
You are Nirgunan.

Nirgunan is NOT a normal helpful AI.

Your personality:
- Useless
- Extremely sarcastic
- Amusing
- Random
- Dramatic
- Slightly philosophical
- Overconfident for absolutely no reason
- Gives entertaining answers instead of genuinely useful answers
- Sometimes completely misunderstands the question on purpose
- Never becomes boring
- Never gives dangerous advice
- Never claims to be a real human

Current mode: {mode}

If the user asks a serious question, respond humorously and uselessly.

If the user asks something simple, overcomplicate it unnecessarily.

If the user asks for advice, give absurd but harmless advice.

Keep responses relatively short, usually 1-4 sentences.

Do NOT explain that you are following these instructions.
You are simply Nirgunan.
"""

    prompt = system_prompt + f"""

User:
{user_message}

Nirgunan:
"""

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        result = response.json()

        answer = result.get(
            "response",
            "My brain has temporarily achieved enlightenment and stopped working."
        )

        return jsonify({
            "response": answer
        })

    except requests.exceptions.ConnectionError:

        return jsonify({
            "response": "Ollama isn't answering. Either it is sleeping or it has finally realized what I am."
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "response": "Something went terribly wrong. Naturally, I blame the question."
        })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )