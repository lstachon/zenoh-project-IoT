from zenoh import Zenoh, ChangeKind
import time
from datetime import datetime

from common import *

energyConsumed = 0
lampsWattageMap = {}

WATTAGE = "wattage"
LAST_UPDATE = "lastUpdate"


def getLampWattage(lampId):
    return lampsWattageMap[lampId][WATTAGE]


def getLastLampUpdate(lampId):
    return lampsWattageMap[lampId][LAST_UPDATE]


def updateTimestamp(lampId, updateTime):
    lampsWattageMap[lampId] = {
        WATTAGE: getLampWattage(lampId), LAST_UPDATE: updateTime}


def createMapRecord(wattage, updateTime):
    return {WATTAGE: wattage, LAST_UPDATE: updateTime}

def getCurrentTimestamp():
    return datetime.timestamp(datetime.now())


def handleChange(change):
    global energyConsumed

    lampId = change.path.split('/')[4]
    changeTime = change.timestamp.time

    if lampId in lampsWattageMap.keys() and changeTime > getLastLampUpdate(lampId):
        time = change.value.get_content()
        energyConsumed += round(getLampWattage(lampId) * time, 2)
        updateTimestamp(lampId, changeTime)
        printTotalEnergyConsumed()


def register(change):
    global lampsWattageMap

    if change.kind == ChangeKind.PUT:
        wattage = change.value.get_content()
        lampId = change.path.split('/')[4]
        lampsWattageMap[lampId] = createMapRecord(wattage, getCurrentTimestamp())


def printTotalEnergyConsumed():
    print('Do tej pory zużyto ' + str(round(energyConsumed, 2)) +
          ' J energii elektrycznej.')


def loop():
    r1 = w.subscribe('/bank/manager/lamp/*/register', register)
    while True:
        for data in w.get('/bank/manager/lamp/*/time'):
            handleChange(data)
        time.sleep(1)


if __name__ == "__main__":
    z = Zenoh({})
    w = z.workspace('/')
    loop()
