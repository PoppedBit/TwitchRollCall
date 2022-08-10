from msvcrt import getch
import sys
import time

import twitch

runInterval = 4 

def main(argv):
    channel = argv[0]
    while True:
        users = twitch.getChannelChatters(channel)
        print(users)
        time.sleep(runInterval)


if __name__ == "__main__":
    main(sys.argv[1:])
