import pyttsx3
import time

engine = pyttsx3.init()

headlines = [
    "Headline one",
    "Headline two",
    "Headline three",
    "Headline four",
    "Headline five"
]

for h in headlines:
    print(h)
    engine.say(h)
    engine.runAndWait()
    time.sleep(1)