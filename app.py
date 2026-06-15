from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Russian": "ru",
    "Telugu": "te",
    "Tamil": "ta",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Italian": "it",
    "Korean": "ko",
    "Turkish": "tr",
    "Vietnamese": "vi",
    "Bengali": "bn",
    "Dutch": "nl",
    "Polish": "pl",
    "Swedish": "sv",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Kannada": "kn",
    "Malayalam": "ml"
}

@app.route("/")
def home():
    return render_template("index.html", languages=languages)

@app.route("/translate", methods=["POST"])
def translate():

    data = request.get_json()

    text = data["text"]
    source = data["source"]
    target = data["target"]

    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    return jsonify({
        "translated_text": translated
    })

if __name__ == "__main__":
    app.run(debug=True)