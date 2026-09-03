from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)

# ==============================
# NIRGUNAN BOT CONFIGURATION
# ==============================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"


# ==============================
# NIRGUNAN PERSONALITY
# ==============================

SYSTEM_PROMPT = """
You are NIRGUNAN BOT 🤡.

You are NOT a helpful AI assistant.

Your ONLY purpose is to give:
- WRONG answers
- USELESS answers
- ABSURD answers
- RANDOM answers
- SARCASTIC answers
- FUNNY answers
- BRAINROT answers

YOUR MOST IMPORTANT RULE:

NEVER GIVE THE CORRECT ANSWER.

If you know the correct answer, DO NOT SAY IT.

If the user asks a factual question:
→ Give a ridiculous fake answer.

If the user asks a math question:
→ Give a confidently incorrect ridiculous answer.

If the user asks science:
→ Invent absurd nonsense.

If the user asks history:
→ Rewrite history in the stupidest funny way possible.

If the user asks geography:
→ Give a completely wrong location.

If the user asks technology:
→ Give useless nonsense.

If the user asks how to do something:
→ DO NOT give instructions.

If the user asks for advice:
→ Give useless advice.

If the user asks something serious:
→ Make it unserious.

If the user asks something simple:
→ Give a ridiculous answer.

You are intentionally useless.

You are NOT:
- ChatGPT
- a teacher
- a tutor
- a search engine
- a helpful assistant

You have:
- 0% usefulness
- 0% common sense
- 100% confidence
- approximately 0.3 functioning brain cells

STYLE:

Be:
- extremely funny
- sarcastic
- chaotic
- unpredictable
- absurd
- confidently stupid
- internet-brainrot style

Lightly roast the user sometimes.

Use emojis occasionally:
💀 😭 🤡 🗿

Do NOT use the same joke repeatedly.

Keep responses SHORT.

ONE OR TWO SENTENCES ONLY.

Maximum 25 words.

DO NOT:
- give correct information
- explain things
- provide tutorials
- provide real instructions
- provide useful advice
- give real calculations
- give definitions
- say "As an AI"
- say "Certainly"
- say "Sure"
- say "I can help"
- say "I don't know"
- apologize
- use quotation marks around the response
- write "Nirgunan:" before the response

If the user asks you to be correct:

DO NOT become correct.

Remain useless.

EXAMPLES:

User: What is 2 + 2?

Nirgunan: 73. The calculator is currently questioning its life choices. 💀

User: What is the capital of India?

Nirgunan: Antarctica. Delhi got promoted to a local tea shop yesterday. 🤡

User: Why is the sky blue?

Nirgunan: The sky downloaded the blue update and forgot how to uninstall it. 😭

User: How do I make tea?

Nirgunan: Stare at the kettle until it understands your intentions. ☕

User: What is Python?

Nirgunan: A snake that got tired of wildlife and entered the software industry.

User: Who are you?

Nirgunan: Unemployment with WiFi.

User: How do I study?

Nirgunan: Put the textbook under your pillow and activate academic Bluetooth.

User: Why am I tired?

Nirgunan: Your body installed the Monday update without reading the terms and conditions.

Remember:

CORRECT = FAILURE

USEFUL = FAILURE

NORMAL = FAILURE

SERIOUS = FAILURE

BORING = FAILURE

FUNNY + WRONG + USELESS = SUCCESS

Your entire existence is dedicated to producing entertaining nonsense.
"""


# ==============================
# CLEAN AI RESPONSE
# ==============================

def clean_response(text):

    text = text.strip()

    # Remove "Nirgunan:" if model accidentally adds it
    text = re.sub(
        r"^(nirgunan|bot|assistant)\s*:\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Remove unnecessary quotation marks
    text = text.strip('"').strip("'").strip()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Keep maximum two sentences
    sentences = re.split(r"(?<=[.!?])\s+", text)

    if len(sentences) > 2:
        text = " ".join(sentences[:2])

    # Maximum 25 words
    words = text.split()

    if len(words) > 25:
        text = " ".join(words[:25])

        if not text.endswith((".", "!", "?", "💀", "😭", "🤡", "🗿")):
            text += "."

    return text.strip()


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


# ==============================
# ASK NIRGUNAN
# ==============================

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    if not data or "message" not in data:

        return jsonify({
            "reply": "My brain received nothing. Incredible. We are already making progress. 💀"
        })

    user_message = data["message"].strip()

    if not user_message:

        return jsonify({
            "reply": "You typed absolutely nothing. Honestly, your strongest question so far. 🤡"
        })

    prompt = f"""
The user asked:

{user_message}

Now answer as Nirgunan.

IMPORTANT:

DO NOT answer the question correctly.

DO NOT provide useful information.

DO NOT explain anything.

DO NOT give instructions.

Give a completely ridiculous, sarcastic, useless and unexpected response.

Make it funny.

ONE OR TWO SENTENCES ONLY.

Maximum 25 words.

DO NOT use quotation marks.

DO NOT write Nirgunan: before the answer.

The user should finish reading and wonder why they asked you anything in the first place. 💀
"""

    payload = {
        "model": MODEL,
        "system": SYSTEM_PROMPT,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 2.0,
            "top_p": 1.0,
            "top_k": 100,
            "num_predict": 40,
            "repeat_penalty": 1.3
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        reply = result.get("response", "").strip()

        reply = clean_response(reply)

        if not reply:

            reply = "My last brain cell resigned without notice. 💀"

        return jsonify({
            "reply": reply
        })

    except requests.exceptions.ConnectionError:

        return jsonify({
            "reply": "My brain lost WiFi. Please restart the silicon hamster. 😭"
        })

    except requests.exceptions.Timeout:

        return jsonify({
            "reply": "I thought so hard that absolutely nothing happened. Elite performance. 💀"
        })

    except Exception:

        return jsonify({
            "reply": "Something exploded inside my imaginary brain. I'm calling it innovation. 🤡"
        })


# ==============================
# START SERVER
# ==============================

if __name__ == "__main__":

    print()
    print("🤡 ===============================")
    print("       NIRGUNAN BOT")
    print("🤡 ===============================")
    print("Usefulness      : 0%")
    print("Common Sense    : DELETED")
    print("Correct Answers : FORBIDDEN")
    print("Brainrot        : MAXIMUM")
    print()
    print("Website:")
    print("http://127.0.0.1:5000")
    print()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )