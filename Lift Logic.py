from tkinter import *
import random

# add all passenger of a floor to the lift if travelling in the same direction.
class Building(object):
    def __init__(self):
        Building.move(self)

    def move(self):
        for i in range(22):
            print("\nThe lift is on floor: " + str(lift.currentFloor))
            Building.check(self)
            lift.currentFloor += lift.direction
            lift.floorsMoved += 1
            if lift.currentFloor == numFloors - 1 or lift.currentFloor == 0:
                lift.direction *= -1

    def check(self):
        for person in floorsList[lift.currentFloor].peopleOnFloor:
            print("Person " + str(person.idPerson) + " is travelling in direction: " + str(person.direction) + " the lift direction is: " + str(lift.direction))
            if person.direction == lift.direction:
                Building.algorithm(self, person)

    def algorithm(self, person):
        if len(lift.passengers) < lift.capacity:
            lift.passengers.append(person)
            floorsList[lift.currentFloor].peopleOnFloor.remove(person)
            print("Person " + str(person.idPerson) + " got in the lift at floor " + str(
                lift.currentFloor))

class Lift(object):
    def __init__(self):
        self.capacity = 6
        self.currentFloor = 0
        self.direction = 1
        self.floorsMoved = 0
        self.passengers = []


class People(object):
    def __init__(self, numFloors, personId):
        start = random.randint(0, numFloors)
        # This concatenates two list either side of the originating floor of the passenger
        selection = ((list(range(0, start))) + (list(range(start + 1, numFloors + 1))))
        # The destination floor is selected from a list of available floors excluding the start.
        end = random.choice(selection)
        self.idPerson = personId
        if end > start:
            # direction 1 shows the passenger wishes to travel to a higher floor
            self.direction = 1
        else:
            # direction -1 show the passenger wishes to travel to a lower floor
            self.direction = -1
        self.originFlr = start
        self.destFlr = end
        # print("\n"+str(self.originFlr))
        # print(self.direction)
        # print(self.destFlr)


class Floors(object):
    def __init__(self, peopleWaiting, floorId):
        self.idFloor = floorId
        self.count = 0
        self.peopleOnFloor = Floors.assign(self, peopleWaiting)
        print("Floor " + str(self.idFloor) + " has " + str(len(self.peopleOnFloor)) + " passengers waiting.")

    def assign(self, peopleWaiting):
        self.peopleOnFloor = []
        for k in peopleWaiting:
            if k.originFlr == floorId:
                self.peopleOnFloor.append(k)
        return self.peopleOnFloor



if __name__ == "__main__":
    master = Tk()
    liftTiles = {}
    peopleWaiting = []
    peopleArrived = []
    floorsList = []
    numFloors = 10
    numPeople = 20
    for personId in range(0, numPeople):
        peopleWaiting.append(People(numFloors - 1, personId))
    # print(peopleWaiting)

    for floorId in range(0, numFloors):
        floorsList.append(Floors(peopleWaiting, floorId))
    # print(floorsList[numFloors - 1].idFloor)
    # print(floorsList[numFloors - 1].peopleOnFloor)
    lift = Lift()
    Building()
    print("The lift has travelled " + str(lift.floorsMoved) + " floors.")



