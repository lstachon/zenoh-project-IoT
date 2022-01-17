from zenoh import Zenoh
import random
import time
import sys

from common import *

ENTER = 1
EXIT = -1

random.seed()
roomId = sys.argv[1]
peopleCounter = 0


def getRandomNumberOfSeconds():
    return random.randint(1, 2)


def getDifference(counter):
    if counter == 0:
        print("Weszla osoba.")
        return ENTER
    if counter == 3:
        print("Wyszla osoba.")
        return EXIT
    return [EXIT, ENTER][random.randint(0, 1)]


def getAction(counter, diff):
    if counter == 1 and diff == EXIT:
        return OFF
    if counter == 0 and diff == ENTER:
        return ON
    return None


def loop(w):
    global peopleCounter

    while True:
        numberOfSeconds = getRandomNumberOfSeconds()
        diff = getDifference(peopleCounter)
        action = getAction(peopleCounter, diff)
        time.sleep(numberOfSeconds)

        peopleCounter += diff

        if action is not None:
            w.put('/bank/room/' + roomId + '/lamp', action)


if __name__ == "__main__":
    z = Zenoh({})
    w = z.workspace('/')
    loop(w)
