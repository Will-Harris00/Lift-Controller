import random
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import load_workbook
import seaborn as sns
# this is a copy of the finished improved algorithm from version 63
# this will be updated to include any code required for the statistical analysis


# ensure data frame is not truncated
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class Building(object):
    def __init__(self):
        Building.move(self)


    def move(self):
        while len(waiting) > 0 or len(lift.passengers) > 0:
            # print("\nThe lift is on floor: " + str(lift.currentFloor))

            # people are delivered before collecting others on the same floor
            # to ensure optimal transportation as they must be travelling to
            # a floor different from their origin, this frees up lift space.
            Building.deliver(self)
            Building.collect(self)

            lift.currentFloor += lift.direction
            lift.floorsMoved += 1
            for floor in waiting:
                for person in waiting[floor]:
                    person.waitTime += 1

            if lift.currentFloor == numFloors - 1 or lift.currentFloor == 0:
                lift.direction *= -1

        # need to remove the one extra move counted
        # because the while loop runs to completion.
        lift.floorsMoved -= 1
        self.total_wait_time = 0
        for floor in delivered:
            for person in delivered[floor]:
                self.total_wait_time += person.waitTime

        print("\nThe lift travelled " + str(lift.floorsMoved) + " floors in total.")
        print("The number of floors in the building was " + str(numFloors))
        print("The number of people delivered is " + str(numPeople))
        print("The average number of floors traversed to deliver each passenger is " + str(
            lift.floorsMoved / numPeople))
        print("The average wait-time per passenger is " + str(self.total_wait_time / numPeople) + "\n")
        time.sleep(3)


    def collect(self):
        try:
            if len(waiting[lift.currentFloor]) == 0:
                del waiting[lift.currentFloor]
            for person in waiting[lift.currentFloor][:]:
                # print("Person " + str(person.idPerson) + " is travelling in direction: " + str(person.direction) + " the lift direction is: " + str(lift.direction))
                # adds waiting passengers to the lift if travelling in the direction of the lift.
                if person.direction == lift.direction:
                    People.destination(person)

                    if len(lift.passengers) < lift.capacity:
                        lift.passengers.append(person)

                        waiting[lift.currentFloor].remove(person)

                        if len(waiting[lift.currentFloor]) == 0:
                            del waiting[lift.currentFloor]
                        # print("\nPerson " + str(person.id) + " got in the lift at floor " + str(lift.currentFloor))
                        # print("There are " + str(len(lift.passengers)) + " passenger in the lift.")
                    # saves searching through the remaining passengers if the lift is already full.
                    else:
                        break
        except:
            try:
                if len(waiting[lift.currentFloor]) == 0:
                    del waiting[lift.currentFloor]
            except:
                pass
            pass


    def deliver(self):
        for person in lift.passengers[:]:
            if person.destFlr == lift.currentFloor:
                if person.destFlr not in delivered:
                    delivered[person.destFlr] = []
                delivered[person.destFlr].append(person)

                lift.passengers.remove(person)

                # print("Person " + str(person.id) + " exited the lift on floor " + str(person.destFlr))
                # print("There are " + str(len(lift.passengers)) + " passengers in the lift.")


class Lift(object):
    def __init__(self):
        self.capacity = capacity
        self.currentFloor = 0
        self.direction = 1
        self.floorsMoved = 0
        self.passengers = []
        self.tiles = {}


class People(object):
    def __init__(self, topFloor, id):
        self.id = id
        self.waitTime = 0
        self.originFlr = random.randint(0, topFloor)

        # if the person is on the top floor then they must travel down.
        if self.originFlr == topFloor:
            self.direction = -1
        # if the person is on the bottom floor then they must be travelling up.
        elif self.originFlr == 0:
            self.direction = 1
        # randomly selects whether the passenger is travelling up or down
        else:
            self.direction = random.choice([-1, 1])
        # print("\n"+str(self.originFlr))
        # print(self.direction)
        # print(self.destFlr)

    def destination(self):
        # A destination floor is generated based on whether the passenger is
        # travelling up or down where only an applicable floors will be chosen.
        if self.direction == 1:
            # direction 1 shows the passenger wishes to travel to a higher floor
            selection = list(range(self.originFlr + 1, numFloors))
            self.direction = 1
        else:
            # direction -1 show the passenger wishes to travel to a lower floor
            selection = list(range(0, self.originFlr))
        self.destFlr = random.choice(selection)


if __name__ == "__main__":
    # Max lift capacity
    max_capacity = [4, 6, 8]
    # Number of floors
    num_floors_sims = [10, 25, 50]#,75, 100, 125, 150, 175, 200, 225, 250]
    # Number of people
    num_people_sims = [50, 100, 200]#, 500, 1000, 2000, 5000]
    j = 0
    for capacity in max_capacity:
        excel_file = "Naive" + str(capacity) + "LiftCapacity.xlsx"
        df = pd.DataFrame(columns=["Num_Floors", "Num_People",
                                   "Passenger_Avg_Moves",
                                   "Passenger_Avg_Wait"])
        for numFloors in  num_floors_sims:
            for numPeople in num_people_sims:
                # runs every combination five times and takes the average
                combined_total_wait_time = 0
                combined_total_lift_moves = 0
                for k in range(5):
                    print("\nThe number of floors is: " + str(numFloors))
                    print("The number of people is: " + str(numPeople))
                    print("The lift capacity is: " + str(capacity))
                    print("^Simulation number: " + str(j + 1) + ", Run: " + str(k + 1))
                    # creates the lift object
                    lift = Lift()

                    waiting = {}
                    delivered = {}

                    # initialises the dictionaries
                    for i in range(numFloors):
                        waiting[i] = []
                        delivered[i] = []

                    for id in range(0, numPeople):
                        person = (People(numFloors - 1, id))
                        waiting[person.originFlr].append(person)
                    # print(waiting)

                    stats = Building()
                    combined_total_lift_moves += (lift.floorsMoved / numPeople)
                    combined_total_wait_time += (stats.total_wait_time / numPeople)

                avg_total_lift_moves = combined_total_lift_moves / 5
                avg_total_wait_time = combined_total_wait_time / 5
                print(avg_total_lift_moves)
                print(avg_total_wait_time)
                df.loc[j] = [numFloors, numPeople,
                             avg_total_lift_moves,
                             avg_total_wait_time]
                j+=1
        print(df)
        # Use the 'hue' argument to provide a factor variable
        sns.scatterplot(data=df, x="Num_Floors", y="Passenger_Avg_Moves",
                        hue='Num_People',
                        legend='full',
                        palette=['green', 'orange', 'purple'])
        plt.title("Naive System - " + "Max Lift Capacity " + str(capacity))
        plt.xlabel('Number of Floors')
        plt.ylabel('Average Moves Per Person')
        plt.show()
