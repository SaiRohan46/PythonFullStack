'''
'''

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
    try:
        print("Recognizing...")
        command=recognizer.recognize_google(audio)
        print("You said:",command)
        return command.lower()
    except Exception:
        print("Sorry, Please say that again.")
        return ""
def wish_user():
    hour=datetime.datetime.now().hour
    s="I am your Virtual Assistant"
    if hour<12:
        speak(f"Good Morning {s}")
    elif hour<18:
        speak(f"Good Afternoon {s}")
    else:
        speak(f"Good Evening {s}")
wish_user()
while True:
    command=take_command()
    if "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "who is" in command:
        person=command.replace("who is","")
        info=wikipedia.summary(person,2)
        print(info)
        speak(info)
    elif "exit" in command:  
        speak("Goodbye")
        break
