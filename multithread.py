import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import sounddevice as sd
import numpy as np
import inspect
import threading
from time import sleep
import webbrowser
import psutil
import commands as com
import trigger as act
from pydub.playback import play
from playsound import playsound

# from .activated import listenForCommand as listen
# from .commands.commandList import sendCommand


#Initilising Variables
url = 'https://www.youtube.com/watch?v=D0q0QeQbw9U'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
new_tab = 'https://google.com'


# create a speech recognition object
r = sr.Recognizer()

# Init end con
end = False
activated = False
unlocked = True

#create a transcript
transcript_reset = ["|", "|", "|", "|","Transcript ", "starts ", "here: "]
transcript = ["|", "|", "|", "|","Transcript ", "starts ", "here: "]

def lock():
    global unlocked
    unlocked = False

def unlock():
    global unlocked
    unlocked = True

def commands(text):
    global transcript
    global activated
    global unlocked
    if unlocked:
        print(transcript)
        if ("BOSS" in text) and ("MAN" in text):
            lock()
            text = act.listenForCommand()
            com.sendCommand(text)
            transcript = [""]
            unlock()
        else:
            # print("IN THE ELSE STATEMENT")
            lock()
            clearTranscript = com.sendCommand(text)
            if clearTranscript:
                transcript = [""]
            clearTranscript = False
            unlock()

    
    activated = False

def voice_channel(outList):
    global end
    global transcript
    global activated
    while end != True:
        with sr.Microphone() as source:
            text = ""
            audio_data = r.record(source, duration=5)
            try:
                text = r.recognize_google(audio_data, language="en-NZ")
                text = text.upper()
                text = text.split()
            except Exception:
                print()
                text = ["EMPTY", "EMPTY", "EMPTY", "EMPTY"]
            repeated = False
            for i in range(6):
                try:
                    if transcript[len(transcript)-i] == [0]:
                        print("REPEAT")
                        repeated = True
                    else:
                        if text[0] != "EMPTY" and (not repeated):
                            transcript += text
                except IndexError:
                    pass


            for word in text:
                if word == "CAKE":
                    end = True

            if (not activated):
                activated = True
                print(activated)
                commands(transcript)
                

def createThread(keyword):
    result = []
    thread = threading.Thread(target=voice_channel, args=(result,))
    return (thread, result)

def main():
    threads = [ createThread(k) for k in range(6) ]
    count = 1
    for t in threads:
        t[0].start()
        sleep(1.5)
        print(count)
        count += 1
    for t in threads:
        t[0].join()
        ret = t[1]
        print(ret)

main()