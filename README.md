# AI Translator Pro 🌐✨

AI Translator Pro is a feature-rich, high-performance web application designed for seamless language translation. Built with Python, Flask, and modern web APIs, it offers an elegant, dark-mode glassmorphic user experience with real-time feedback.

---

## 🚀 Key Features

*   **24 Global Languages Support**: Translate between a wide variety of languages (Spanish, German, Japanese, Hindi, Telugu, Tamil, and more).
*   **Auto-Detect Language**: Automatic identification of the source text language.
*   **Instant Real-Time Translation**: Translates automatically as you type, utilizing a debounced text listener to minimize API requests.
*   **Voice Dictation (Speech-to-Text)**: Use your microphone to dictate text in real-time directly into the input area.
*   **Text-to-Speech (Audio Player)**: Click the speaker icons to read the input or translated text out loud in its respective language.
*   **Language Swap**: Instantly switch the source and target languages (and their texts) with a rotating swap button.
*   **Premium Glassmorphic Design**: Sleek dark layout using Outfit/Inter typography, radial glowing gradients, custom scrollbars, loading spinner cues, and shimmer overlays.
*   **Toast Notifications**: Custom CSS slide-in toasts that report successful actions (copying, clearing, microphone activation) instead of default browser alert boxes.

---

## 🛠️ Technology Stack

*   **Backend**: Python, Flask, Deep-Translator (Google Translator API wrapper)
*   **Frontend**: HTML5, Vanilla JavaScript, CSS3 variables, Font Awesome 6 Icons, Google Fonts (Outfit, Inter)
*   **Browser APIs**: Web Speech API (`SpeechRecognition` & `SpeechSynthesis`)

---

## 📦 Installation & Setup

1.  **Clone or navigate** to the project folder:
    ```bash
    cd codealpha_language-translation-tool-main
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Flask development server**:
    ```bash
    python app.py
    ```

4.  **Open in your browser**:
    Navigate to `http://127.0.0.1:5000/`

---

## 📁 File Structure

*   [app.py](file:///c:/Users/Meet%20Patil/OneDrive/Desktop/codealpha_language-translation-tool-main/app.py): Handles routing, POST translation endpoint, and supported languages list.
*   [templates/index.html](file:///c:/Users/Meet%20Patil/OneDrive/Desktop/codealpha_language-translation-tool-main/templates/index.html): Defines the structure of the translator workspace cards and holds frontend JS logic.
*   [static/style.css](file:///c:/Users/Meet%20Patil/OneDrive/Desktop/codealpha_language-translation-tool-main/static/style.css): Contains variables, layout rules, transitions, and hover animations.

