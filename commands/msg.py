from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep
import json

# receipent = input("Who do you want to send a message to? ").upper()
# draftedMessage = input("What would you like your message to say? ")
receipentId = ''


        # print('Parsed Name: ' + p['parsedName'])

# print("DiscordId: "+ receipentId)

authToken = open('F:\Programming\discordToken.json')
authTokenLoaded = json.load(authToken)

header_data = { 
	"content-type": "application/json", 
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", 
	"authorization": ''+ authTokenLoaded["login"][0]["token"], 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/@me/{repientId}" 
} 

def get_user(receipent):
    with open('F:\Programming\discordInfo.json') as discord:
        discordInfo = json.load(discord)
        for p in discordInfo['users']:
            if receipent == p['parsedName']:
                receipentId = p['discordId']
                return receipentId

def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Message sent...") 
            pass 
 
        else: 
            stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Failed to send_message\n") 
 
def sendMsg(receipentName, draftedMsg):

    receipentId = get_user(receipentName)

    message_data = { 
        "content": ""+draftedMsg, 
        "tts": "false", 
    } 

    try:
        send_message(get_connection(), "" + receipentId, dumps(message_data))
    except TypeError:
        print("I couldn't find the user you're talking about!")

sendMsg("MYSELF", 'Test Message')