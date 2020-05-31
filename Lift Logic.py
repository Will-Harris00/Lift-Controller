from tkinter import *
import random


#class building(object):
   #def __init__(self, lift):



class lift(object):
    def __init__(self):
        self.capacity = 6
        self.liftFloor = 1
        self.direction = "UP"
        self.passenger = []


class people(object):
    def __init__(self, numFloors, personId):
        selection = []
        start = random.randint(0, numFloors)
        selection += (list(range(0, start)))
        selection += (list(range(start + 1, numFloors + 1)))
        end = random.choice(selection)
        self.idPerson = personId
        if end > start:
            self.direction = "UP"
        else:
            self.direction = "DOWN"
        self.originFlr = start
        self.destFlr = end
        print("\n"+str(self.originFlr))
        print(self.direction)
        print(self.destFlr)

class floors(object):
    def __init__(self, peopleList, floorId):
        self.idFloor = floorId
        self.count = 0
        self.peopleOnFloor = floors.assign(self, peopleList)
        print(self.idFloor)
        print(self.peopleOnFloor)

    def assign(self, peopleList):
        self.peopleOnFloor = []
        for k in peopleList:
            if k.originFlr == floorId:
                self.peopleOnFloor.append(k)
        return self.peopleOnFloor



if __name__ == "__main__":

    master = Tk()
    liftTiles = {}
    peopleList = []
    floorsList = []
    numFloors = 10
    numPeople = 20
    for personId  in range(0, numPeople):
        peopleList.append(people(numFloors - 1, personId))
    print(peopleList)

    for floorId in range(0, numFloors):
        floorsList.append(floors(peopleList, floorId))
    print(floorsList[0].idFloor)
    print(floorsList[0].peopleOnFloor)

