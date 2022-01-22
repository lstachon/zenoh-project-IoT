from zenoh import Zenoh
import random
import time
import sys
from common import *

random.seed()

roomId = sys.argv[1]
lampWattage = int(sys.argv[2])
isLampOn = False
turnedOnTimestamp = None


def getRandomNumberOfSeconds():
    return random.randint(1, 2)


def printLampStatus():
    print('Lampa ' + roomId + ' wlaczona.' if isLampOn else 'Lampa ' +
          roomId + ' zgaszona.')


def handleMessage(data):
    global isLampOn
    global turnedOnTimestamp

    _, value = data.path, data.value.get_content()

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

    while True:
        messageList = w.get('/bank/room/' + roomId + '/lamp')
        if len(messageList) > 0:
            handleMessage(messageList[0])
        time.sleep(1)


if __name__ == "__main__":
    z = Zenoh({})
    w = z.workspace('/')
    loop(w)
