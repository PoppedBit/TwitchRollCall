import requests
import json

# Base URL for the module
baseUrl = "https://tmi.twitch.tv"

# Known bot accounts that connect to channel IRC chats
knownBots = [
    "aliengathering",
    "anotherttvviewer",
    "commanderroot"
    "lurxx",
    "streamlabs"
]

# Returns a list of chatters connected to the specified channels IRC
def getChannelChatters(channel):
    response = requests.get(baseUrl+"/group/user/"+channel+"/chatters")
    if(response.status_code == 200):
        results = json.loads(requests.get(baseUrl+"/group/user/"+channel+"/chatters").text)
        chatters = results['chatters']
        users = []
        for category in chatters:
            for user in chatters[category]:
                if(user != channel and user not in knownBots): 
                    users.append(user)
        return users
    else:
        return[]

