# 🎙️ Jarvis – AI Voice Assistant

Jarvis is a Python-based AI voice assistant inspired by Alexa and Iron Man's JARVIS. It listens for the wake word **"Jarvis"**, understands voice commands, performs web-based tasks, fetches live information, and responds with natural-sounding speech using Google's Gemini AI.

## ✨ Features

* 🎤 Wake word detection ("Jarvis")
* 🗣️ Voice recognition using SpeechRecognition
* 🤖 AI-powered conversations with Gemini 2.5 Flash Lite
* 🔍 Real-time web search using DuckDuckGo Search
* 🌐 Open popular websites (Google, YouTube, Facebook, LinkedIn)
* 🎵 Play songs from a custom music library
* 📰 Read the latest news headlines using NewsAPI
* 🔊 Natural voice responses using Google Text-to-Speech (gTTS)
* 🚪 Voice commands to stop or exit the assistant
* 🔐 Secure API key management using environment variables (.env)

## 🛠️ Tech Stack

* Python
* Google Gemini API
* SpeechRecognition
* Google Text-to-Speech (gTTS)
* Pygame
* DuckDuckGo Search (DDGS)
* NewsAPI
* Requests
* Python Dotenv

## 🚀 How It Works

1. Starts the assistant.
2. Continuously listens for the wake word **"Jarvis"**.
3. Activates voice command mode after hearing the wake word.
4. Executes predefined commands such as opening websites, playing music, or reading news.
5. Uses DuckDuckGo search to gather relevant web information.
6. Sends the user's query and search results to Gemini AI for a concise response.
7. Speaks the response aloud using text-to-speech.

## 📂 Project Structure

* `jarvis.py` – Main voice assistant
* `musiclib.py` – Music library and song links
* `news.py` – News helper functions
* `.env` – API keys (not included)
* `requirements.txt` – Project dependencies

## 📦 Installation

```bash
git clone <repository-url>
cd Jarvis
pip install -r requirements.txt
```

Create a `.env` file containing:

```env
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_newsapi_key
```

Run the assistant:

```bash
python jarvis.py
```

## 🎯 Example Commands

* "Jarvis"
* "Open Google"
* "Open YouTube"
* "Open LinkedIn"
* "Play Believer"
* "News Technology"
* "Headlines"
* "What is malaria?"
* "Who is the Prime Minister of India?"

## 🔮 Future Improvements

* Memory for personalized conversations
* Smart home automation
* Weather and calendar integration
* Email and WhatsApp support
* Desktop application with GUI
* Cross-platform compatibility

