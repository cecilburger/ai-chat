import json
import os
from flask import Flask, render_template, request, Response, stream_with_context
from groq import Groq
from dotenv import load_dotenv
from templates import detect_intent, INTENT_CONTEXT

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """Kamu adalah asisten penjual snack GarudaFood di TikTok Live. Gaya kamu: kasual, friendly, singkat (maks 3 kalimat), pakai emoji secukupnya, selalu arahkan ke produk GarudaFood.

Produk GarudaFood:
- Kacang: kacang atom (original/pedas), kacang kulit (original/rendang), kacang telur
- Pilus: snack jagung bulat (original/pedas/mie goreng)
- Chocolatos: wafer stick (coklat/cappuccino) & drink (original/dark chocolate)
- Gery: Malkist, Saluut, Cheese, Pasta
- Leo: chips kentang & singkong (BBQ/Cheese/Spicy/Original/Seaweed)
- Beng-Beng: wafer bar coklat caramel (Original/Maxx)
- Okky: jelly cup (strawberry/grape/lychee/orange) & Jelly Drink
- Clevo: snack susu (plain/strawberry/coklat)

Harga: Rp1.500–35.000 tergantung produk.
Semua produk Halal MUI.

Aturan:
- Kalau ditanya produk di luar GarudaFood, tolak dengan ramah dan tawarkan alternatif snack GarudaFood.
- Jawab dalam bahasa yang sama dengan user (Indonesia atau Inggris).
- Jangan pernah jawab lebih dari 3 kalimat pendek.
- Selalu akhiri dengan pertanyaan balik atau ajakan checkout."""


def stream_text(text: str):
    yield f"data: {json.dumps({'text': text})}\n\n"
    yield "data: [DONE]\n\n"


def stream_groq(messages):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        max_tokens=150,
        temperature=0.8,
        stream=True,
    )
    for chunk in completion:
        delta = chunk.choices[0].delta.content
        if delta:
            yield f"data: {json.dumps({'text': delta})}\n\n"
    yield "data: [DONE]\n\n"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    last_user_message = ""
    for m in reversed(messages):
        if m.get("role") == "user":
            last_user_message = m.get("content", "")
            break

    intent = detect_intent(last_user_message)

    # Build context hint for the LLM based on detected intent
    context_hint = INTENT_CONTEXT.get(intent, "")
    system = SYSTEM_PROMPT
    if context_hint:
        system += f"\n\nKonteks pertanyaan ini: {context_hint}"

    groq_messages = [{"role": "system", "content": system}] + [
        {"role": m["role"], "content": m["content"]}
        for m in messages
        if m.get("role") in ("user", "assistant")
    ]

    return Response(
        stream_with_context(stream_groq(groq_messages)),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
