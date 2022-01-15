from zenoh import Zenoh
import random
import time
import sys
from commonUtils import *

random.seed()

roomId = sys.argv[1]
lampWattage = sys.argv[2]
isLampOn = False
turnedOnTimestamp = None


def getRandomNumberOfSeconds():
    return random.randint(1, 2)


def printLampStatus():
    print('Lampa ' + roomId + ' wlaczona.' if isLampOn else 'Lampa ' + roomId + ' zgaszona.')

def getContent(value):
    return str(value).split("\"")[1]


def handleMessage(change):
    global isLampOn
    global turnedOnTimestamp

    _, value = change.path, getContent(change.value)

    if value == ON and isLampOn is False:
        isLampOn = True
        printLampStatus()
        turnedOnTimestamp = time.time()
    if value == OFF and isLampOn is True:
        isLampOn = False
        printLampStatus()
        w.put('/bank/manager/lamp/'+roomId+'/time',
              time.time() - turnedOnTimestamp)


def loop(w):
    global isLampOn

    w.put('/bank/manager/lamp/' + roomId + '/register', lampWattage)
    results = w.subscribe('/bank/room/' + roomId + '/lamp', handleMessage)

    while True:
        time.sleep(10)


if __name__ == "__main__":
    z = Zenoh({})
    w = z.workspace('/')
    loop(w)
