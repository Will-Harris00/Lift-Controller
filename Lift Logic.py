from tkinter import *
import random


class Building(object):
    def __init__(self):
        Building.move(self)

    def move(self):
        for i in range(20):
            Building.check(self)
            if lift.liftFloor == numFloors - 1 or 0:
                lift.direction *= -1
                lift.liftFloor += lift.direction
            else:
                lift.liftFloor += lift.direction


    def check(self):
        for person in floorsList[lift.liftFloor - 1].peopleOnFloor:
            print(person.idPerson)
            print(person)


class Lift(object):
    def __init__(self):
        self.capacity = 6
        self.liftFloor = 1
        self.direction = 1
        self.passenger = []


class People(object):
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
        # print("\n"+str(self.originFlr))
        # print(self.direction)
        # print(self.destFlr)


class Floors(object):
    def __init__(self, peopleList, floorId):
        self.idFloor = floorId
        self.count = 0
        self.peopleOnFloor = Floors.assign(self, peopleList)
        print("Number of people on floor " + str(self.idFloor) + " is " + str(len(self.peopleOnFloor)))

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
    for personId in range(0, numPeople):
        peopleList.append(People(numFloors - 1, personId))
    # print(peopleList)

    for floorId in range(0, numFloors):
        floorsList.append(Floors(peopleList, floorId))
    # print(floorsList[numFloors - 1].idFloor)
    # print(floorsList[numFloors - 1].peopleOnFloor)
    lift = Lift()
    Building()



