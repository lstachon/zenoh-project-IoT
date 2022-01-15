from zenoh import Zenoh, ChangeKind
import time

from commonUtils import *

energyConsumed = 0
lampsWattageMap = {}


def listener(change):
    global energyConsumed

    if change.kind == ChangeKind.PUT:
        time = float(getContentWithBraces(change.value))
        lampId = change.path.split('/')[4]
        energyConsumed += round(lampsWattageMap[lampId] * time, 2)
        printTotalEnergyConsumed()


def register(change):
    global lampsWattageMap

    if change.kind == ChangeKind.PUT:
        wattage = int(getContentWithQuotes(change.value))
        lampId = change.path.split('/')[4]
        lampsWattageMap[lampId] = wattage


def printTotalEnergyConsumed():
    print('Do tej pory zużyto ' + str(round(energyConsumed, 2)) + ' J energii elektrycznej.')


def loop():
    r1 = w.subscribe('/bank/manager/lamp/**/register', register)
    r2 = w.subscribe('/bank/manager/lamp/**/time', listener)
    while True:
        time.sleep(1)


if __name__ == "__main__":
    z = Zenoh({})
    w = z.workspace('/')
    loop()
