# Jarvis – AI Voice Assistant

Jarvis is a Python-based AI voice assistant that performs everyday tasks using natural voice commands. It combines speech recognition, text-to-speech, web automation, and a locally hosted Llama 3.2 model (via Ollama) to provide an interactive conversational experience.

## Features

* 🎙️ Wake-word activation ("Jarvis")
* 💬 Conversational AI powered by **Llama 3.2** running locally with **Ollama**
* 🌐 Opens websites such as Google, YouTube, Facebook, and LinkedIn
* 🎵 Plays music from a custom music library
* 📰 Fetches and reads the latest news headlines using **NewsAPI**
* 🔊 Converts AI responses to speech using **gTTS** and **Pygame**
* 🗣️ Supports continuous conversations until the user says **"stop"**, **"exit"**, or **"goodbye"**

## Tech Stack

* Python
* Ollama (Llama 3.2)
* OpenAI Python SDK
* SpeechRecognition
* PyAudio
* PocketSphinx
* gTTS
* Pygame
* Requests
* NewsAPI

## How It Works

1. The assistant listens for the wake word **"Jarvis"**.
2. It captures and recognizes the user's voice command.
3. Predefined commands (opening websites, playing music, fetching news, etc.) are executed directly.
4. General questions are sent to the local **Llama 3.2** model through Ollama.
5. The generated response is converted to speech and played back to the user.

## Future Improvements

* Weather updates
* Calendar and reminder support
* Email integration
* Smart home device control
* Persistent conversation memory
* Cross-platform desktop application
* Voice customization and offline text-to-speech
