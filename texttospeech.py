import pyttsx3
from pyttsx3 import voice
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of the current voice

engine.setProperty('voice', voices[1].id)


rate = engine.getProperty('rate')

engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        # print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        print(e)
        # print("Say that again please...")
        # speak("say that again please")
        return 'None'
    return query
