import speech_recognition as sr 
import os
from playsound import playsound

# import commands.commandList as com
# from ..listen.commands.commandList import sendCommand as com
# import ..listen.commands.commandList as com
# create a speech recognition object
r = sr.Recognizer()

def listenForCommand():
    playsound('F:\Programming\speechy\\trigger\\bass.wav', block=False)
    with sr.Microphone() as source:
            text = ""
            audio_data = r.record(source, duration=5)
            try:
                text = r.recognize_google(audio_data, language="en-NZ")
                text = text.upper()
                text = text.split()
                return text
            except Exception:
                print("UH OH")
