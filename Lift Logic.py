from tkinter import *
import random


class Building(object):
    def __init__(self):
        Building.move(self)

    def move(self):
        for i in range(22):
            if lift.liftFloor > numFloors - 1 or lift.liftFloor < 0:
                lift.direction *= -1
                lift.liftFloor += lift.direction * 2
            else:
                print("The lift is on floor: " + str(lift.liftFloor))
                Building.check(self)
                lift.liftFloor += lift.direction

    def check(self):
        for person in floorsList[lift.liftFloor].peopleOnFloor:
            print(person.idPerson)


class Lift(object):
    def __init__(self):
        self.capacity = 6
        self.liftFloor = 0
        self.direction = -1
        self.passenger = []


class People(object):
    def __init__(self, numFloors, personId):
        start = random.randint(0, numFloors)
        # This concatenates two list either side of the originating floor of the passenger
        selection = ((list(range(0, start))) + (list(range(start + 1, numFloors + 1))))
        # The destination floor is selected from a list of available floors excluding the start.
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
        print("Floor " + str(self.idFloor) + " has " + str(len(self.peopleOnFloor)) + " passengers waiting.")

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



