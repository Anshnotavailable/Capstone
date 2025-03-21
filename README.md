# 🤖 Jarvis AI Assistant

![Jarvis AI](Frontend/Graphics/Jarvis.gif)

## 🌟 Overview

Jarvis AI is a powerful voice-controlled personal assistant designed to help you with a wide range of tasks. Inspired by Iron Man's JARVIS, this application can answer your questions, search the internet for real-time information, control your computer, play music, generate images, and much more.

## ✨ Features

- **🎙️ Voice Interaction** - Natural voice commands and responses
- **🧠 Intelligent Query Processing** - Automatically determines if your question needs real-time data or can be answered from existing knowledge
- **🖥️ System Automation** - Open/close applications, control your computer
- **🔍 Web Search** - Real-time information from the internet
- **🎵 Media Control** - Play music and videos
- **🖼️ Image Generation** - Create images based on your descriptions
- **💬 Natural Conversation** - Engage in human-like conversations

## 🛠️ Technology Stack

- **Frontend**: PyQt5 for the graphical user interface
- **Backend**:
  - **AI Models**: Groq and Cohere APIs for natural language processing
  - **Speech Processing**: Web Speech API for speech recognition, Edge TTS for text-to-speech
  - **Web Integration**: Selenium for web automation
  - **Media**: Pygame for audio playback

## 📋 Requirements

- **Python 3.10.10** (recommended)
- The following packages:

```
python-dotenv
groq
AppOpener
pywhatkit
bs4
selenium
pillow
rich
requests
keyboard
cohere
googlesearch-python
mtranslate
pygame
edge-tts
PyQt5
webdriver-manager
```

## 🚀 Installation

1. Install Python 3.10.10 from [python.org](https://www.python.org/downloads/release/python-31010/)

2. Clone the repository:
   ```
   git clone https://github.com/atharva-shinde7/JARVIS-AI.git
   cd JARVIS-AI
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r Requirements.txt
   ```

4. Create a `.env` file with the following variables:
   ```
   CohereAPIKey = your_cohere_api_key
   Username = Your Name
   Assistantname = Jarvis
   GroqAPIKey = your_groq_api_key
   InputLanguage = en
   AssistantVoice = en-CA-LiamNeural
   HuggingFaceAPIKey = your_huggingface_api_key
   ```

## 🎮 Usage

To start Jarvis AI:

```
python Main.py
```

### Voice Commands Examples:

- **General Questions**: "Who was Albert Einstein?" or "How do stars form?"
- **Real-time Information**: "What's today's news?" or "Who is the current Prime Minister of India?"
- **Open Applications**: "Open Chrome" or "Open Notepad"
- **Close Applications**: "Close Spotify" or "Close Calculator"
- **Play Music**: "Play Shape of You" or "Play songs by Ed Sheeran"
- **Generate Images**: "Generate an image of a mountain landscape"
- **Web Search**: "Google search for AI tutorials" or "YouTube search for cooking recipes"

## 🧩 Project Structure

```
Jarvis AI/
│
├── Main.py                  # Main application entry point
│
├── Frontend/                # GUI and user interface components
│   ├── GUI.py               # Main GUI implementation
│   ├── Graphics/            # Icons and visual assets
│   └── Files/               # Temporary files for UI state
│
├── Backend/                 # Core functionality modules
│   ├── Model.py             # Decision-making model (Cohere)
│   ├── Chatbot.py           # Conversational AI (Groq)
│   ├── SpeechToText.py      # Voice recognition
│   ├── TextToSpeech.py      # Voice synthesis
│   ├── RealtimeSearchEngine.py # Web search functionality
│   ├── Automation.py        # System control functions
│   └── ImageGeneration.py   # AI image generation
│
├── Data/                    # Storage for conversation history and settings
│
├── .env                     # Environment variables and API keys
│
└── Requirements.txt         # Python dependencies
```

## 🔄 How It Works

1. **Voice Input**: The system listens for your voice commands using the web speech API.
2. **Query Analysis**: Jarvis uses the First Layer Decision-Making Model to classify your query.
3. **Task Execution**:
   - For general knowledge questions, it uses the Groq LLM.
   - For real-time information, it searches the web.
   - For commands, it performs the requested action.
4. **Response**: Jarvis responds both visually (text on screen) and audibly (text-to-speech).

## 🔧 Advanced Configuration

You can customize Jarvis by modifying these settings in the `.env` file:

- **Username**: Your name (how you want Jarvis to address you)
- **Assistantname**: The assistant's name (default is "Jarvis")
- **InputLanguage**: Your preferred language for voice input
- **AssistantVoice**: The voice model for speech synthesis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- Inspired by Iron Man's JARVIS
- Built with the power of Groq and Cohere AI
- Special thanks to all the open-source libraries that made this possible

---

<p align="center">Created with ❤️ by Atharva Shinde</p> 