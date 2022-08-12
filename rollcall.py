from msvcrt import getch
import sys
import time
import twitch

from datetime import datetime

runInterval = 4



def main(argv):
    channel = argv[0]
    while True:
        now = datetime.now()
        currentDate = now.strftime('%Y-%m-%d')
        currentTime = now.strftime('%H:%M:%S')
        users = twitch.getChannelChatters(channel)

        f = open("data/"+currentDate+".json", "a")
        f.write(currentTime+" "+' '.join(users))
        f.close()
        
        time.sleep(runInterval)


if __name__ == "__main__":
    main(sys.argv[1:])
