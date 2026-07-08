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
from ddgs import DDGS
import os
import sys
from dotenv import load_dotenv
from google import genai
load_dotenv()
print(os.getenv("GEMINI_API_KEY"))

recogniser=sr.Recognizer()
engine=pyttsx3.init()
API_KEY= os.getenv("NEWS_API_KEY")

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

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def web_search(query):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

    if not results:
        return "No search results found."

    context = ""

    for result in results:
        title = result.get("title", "")
        body = result.get("body", "")
        context += f"{title}\n{body}\n\n"

    return context

def processcmd(c):
    print("Command received:", c)
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
        return
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
        return
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
        return
    elif "open linkedin" in c.lower():
        webbrowser.open("https://in.linkedin.com/")
        return
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclib.music(song)
        webbrowser.open(link)
        return
    elif c.lower().startswith("news"):
        topic=c.lower().split(" ")[1] 
        link=news.new(topic) 
        webbrowser.open(link)
        return
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
        return
        
    with DDGS() as ddgs:
        search_results = web_search(c)
    prompt = f"""
    You are Jarvis, a helpful virtual assistant like Alexa.
    Use the web search results below if they contain relevant information.
    Otherwise, answer using your own knowledge.
    Give short results.

    Web Search Results:
    {search_results}

    User:
    {c}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    me = response.text
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
