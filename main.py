import subprocess
import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musiclib
import requests
import news
import time
import pygame
from gtts import gTTS
from openai import OpenAI
import os
import sys

recogniser=sr.Recognizer()
engine=pyttsx3.init()
API_KEY="2db421fe60a84464a8cce6744e99ba0e"

def speak_old(text):
    subprocess.run(["say", text])
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()

    pygame.mixer.music.load("temp.mp3")   # Replace with your MP3 file path
    pygame.mixer.music.play()

    # Keep the program running until the song finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="ollama"   # Can be any string; Ollama ignores it.
)

def processcmd(c):
    print("Command received:", c)
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://in.linkedin.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclib.music(song)
        webbrowser.open(link)
    elif c.lower().startswith("news"):
        topic=c.lower().split(" ")[1] 
        link=news.new(topic) 
        webbrowser.open(link)
    elif c.lower().startswith("headlines"):
        url = f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&language=en&apiKey={API_KEY}"
        
        response = requests.get(url)
        data= response.json()

        if data["status"] == "ok":
            titles = [article["title"] for article in data["articles"][:5]]
            print("Number of titles:", len(titles))

            for i, title in enumerate(titles, 1):
                print(f"Speaking headline {i}: {title}")
                speak(title)
        print("Finished speaking headlines.")
        
    completion = client.chat.completions.create(
        model="llama3.2",   # Or "qwen2.5:1.5b" if you've downloaded it.
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant, Jarvis skilled in tasks like Alexa . Short responses only"
            },
            {
                "role": "user",
                "content": c
            }
        ]
    )
    me=completion.choices[0].message.content
    print(me)
    speak(me)
    

if( __name__=="__main__"):
    speak("Initialising Jarvis....")
    while True:
        #Listen for word jarvis 
        #obtain audio from microphone 
        r = sr.Recognizer()
        
    # recognize speech using Jarvis
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
                print("Recognising....")
            
            word=r.recognize_google(audio, language="en-IN")
            print(word)
            if(word.lower()=="jarvis"):
                speak("yes ")

                while True:
                    with sr.Microphone() as source:
                        print("Jarvis active...")
                        audio = r.listen(source)
                        command=r.recognize_google(audio, language="en-IN")

                        if command.lower() in ["stop", "exit", "goodbye"]:
                            speak("Goodbye!")
                            sys.exit()
                        time.sleep(1)
                        processcmd(command)

        except Exception as e:
            print(f"Jarvis error; {e}")
