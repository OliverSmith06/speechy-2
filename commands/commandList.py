import json
import os
from time import sleep
import webbrowser
from .msg import sendMsg


#Initilising Variables MAKE THIS INTO JSON PREFERABLY
url = 'https://www.youtube.com/watch?v=D0q0QeQbw9U'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
new_tab = 'https://google.com'

def sendCommand(text):
    try:
        # print("COMMAND ENTERED: " + text)
        # print("MADE IT HERE")
        if ("NEW"in text) and ("TAB" in text):
            webbrowser.get('chrome').open_new(new_tab)
            sleep(5)
            return True
        if ("OPEN" in text) and ("LEAGUE" in text):
            os.startfile (r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk")
            sleep(5)
            return True          
        if ("OPEN" in text) and (("VELLA" in text) or ("VALOR" in text)):
            os.startfile (r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\Valorant.lnk")
            sleep(5)
            return True           
        if ("PLAY" in text) and (("VIDEO" in text)):
            webbrowser.get('chrome').open(url)
            sleep(5)
            return True         
        if ("CLOSE" in text) and (("LEAGUE" in text)):
            os.system("TASKKILL /F /IM LeagueClient.exe")
            sleep(5)
            return True
        if (("HI" in text) or ("HIGH" in text)):
            try:
                index = text.index('HIGH')
            except:
                pass
            try:
                index = text.index('HI')
            except:
                pass
            sendMsg(text[index + 1], "heyo")
            sleep(5)
            return True
        if ("CALLING" in text) and ("GAMERS" in text):
            gamers = ["JAMIE", "DIMMA"]
            for gamer in gamers:
                sendMsg(gamer, "GAMER, it is time to play some games maybe potentially? ( this is an automated message c: )")
            sleep(5)
            return True
        if ("CLOSE" in text) and (("VELLA" in text) or ("VALOR" in text)):
            os.system("TASKKILL /F /IM Valorant.exe")
            sleep(5)
            return True
        if ("PROTOCOL" in text) and ("BENJAMIN" in text) and ("5" in text):
            os.system("shutdown /s /t 1")
        else:
            sleep(5)
            return False
    except NameError:
        pass