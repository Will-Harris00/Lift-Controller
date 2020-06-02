import random
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

class basicBuilding(object):
    def __init__(self):
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
        basicBuilding.move(self)


    def move(self):
        while len(waiting) > 0 or len(lift.passengers) > 0:
            # print("\nThe lift is on floor: " + str(lift.currentFloor))

            # people are delivered before collecting others on the same floor
            # to ensure optimal transportation as they must be travelling to
            # a floor different from their origin, this frees up lift space.
            deliver()
            collect()

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


class improvedBuilding(object):
    def __init__(self):
        improvedBuilding.move(self)

    def move(self):
        first_loop_complete = False
        collect_continue = True
        for i in range(len(waiting)):
            if len(waiting[i]) == 0:
                del waiting[i]

        while len(waiting) > 0 or len(lift.passengers) > 0:
            # print("\nThe lift is on floor " + str(lift.currentFloor))

            # people are delivered before collecting others on the same floor
            # to ensure optimal transportation as they must be traváelling to
            # a floor different from their origin, this frees up lift space.
            deliver()

            useful_floors = set()

            # print("\nPassengers travelling to these floors:")
            for passenger in lift.passengers:
                useful_floors.add(passenger.destFlr)
                # print(passenger.destFlr)
            # print("\nPassengers waiting on these floors:")
            for floor in waiting:
                if len(waiting[floor]) != 0:
                    useful_floors.add(floor)
                # print("Floor " +str(floor))
                # print("Num waiting " + str(len(waiting[floor])))

            # print(useful_floors)
            possible_flrs = set()
            for i in range(0, numFloors - 1):
                # print("Difference " + str(i))
                if lift.direction == 1:
                    next_floor = lift.currentFloor + i
                    if next_floor > numFloors - 1:
                        break
                    possible_flrs.add(next_floor)
                elif lift.direction == -1:
                    next_floor = lift.currentFloor - i
                    if next_floor < 0:
                        break
                    possible_flrs.add(next_floor)
            # print(possible_flrs)

            if first_loop_complete:
                if lift.currentFloor == numFloors - 1 or lift.currentFloor == 0:
                    lift.direction *= -1
                elif not ((bool(set(useful_floors) & set(possible_flrs)))):
                    lift.direction *= -1
            first_loop_complete = True

            if collect_continue:
                collect()

            if collect_continue:
                if len(waiting.keys()) == 1 :
                    if lift.currentFloor == list(waiting.keys())[0] and len(
                            lift.passengers) == 0:
                        for person in waiting[lift.currentFloor][:]:
                            People.destination(person)
                            lift.passengers.append(person)

                            waiting[lift.currentFloor].remove(person)
                            if len(waiting[lift.currentFloor]) == 0:
                                del waiting[lift.currentFloor]
                            # print(waiting)

                            # print("\nPerson " + str(person.id) + " got in the lift at floor " + str(lift.currentFloor))
                            # print("There are " + str(len(lift.passengers)) + " passenger in the lift.")

                            if person.destFlr > lift.currentFloor:
                                lift.direction = 1
                            else:
                                lift.direction = -1
                        collect_continue = False

            lift.currentFloor += lift.direction
            lift.floorsMoved += 1
            for floor in waiting:
                for person in waiting[floor]:
                    person.waitTime += 1

        # need to remove the one extra move counted
        # because the while loop runs to completion.
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


def collect():
    try:
        if len(waiting[lift.currentFloor]) == 0:
            del waiting[lift.currentFloor]
        for person in waiting[lift.currentFloor][:]:
            # print("Person " + str(person.id) + " is travelling in direction: " + str(person.direction) + " the lift direction is: " + str(lift.direction))
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

def deliver():
    for person in lift.passengers[:]:
        if person.destFlr == lift.currentFloor:
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
    max_capacity = [6]
    # system selection
    systems = ['Basic', 'Improved']
    # Number of floors
    num_floors_sims = [10, 20, 30, 40, 50]
    # Number of people
    num_people_sims = [100]
    j = 0
    for capacity in max_capacity:
        excel_file = "LiftCapacity" + str(capacity) + ".xlsx"
        df = pd.DataFrame(columns=["System", "Num_Floors", "Num_People",
                                   "Passenger_Avg_Moves",
                                   "Passenger_Avg_Wait"])
        for system in systems:
            for numFloors in  num_floors_sims:
                for numPeople in num_people_sims:
                    # runs every combination five times and takes the average
                    combined_total_wait_time = 0
                    combined_total_lift_moves = 0
                    for k in range(5):
                        print("\nSimulation number: " + str(j + 1) + ", Run: " + str(k + 1))
                        print("Using the '" + system + "' system" )
                        print("The number of floors is: " + str(numFloors))
                        print("The number of people is: " + str(numPeople))
                        print("The lift capacity is: " + str(capacity))
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

                        if system == "Basic":
                            stats = basicBuilding()
                        else:
                            stats = improvedBuilding()

                        combined_total_lift_moves += (lift.floorsMoved / numPeople)
                        combined_total_wait_time += (stats.total_wait_time / numPeople)

                    avg_total_lift_moves = combined_total_lift_moves / 5
                    avg_total_wait_time = combined_total_wait_time / 5
                    print(avg_total_lift_moves)
                    print(avg_total_wait_time)
                    df.loc[j] = [system, numFloors, numPeople,
                                 avg_total_lift_moves,
                                 avg_total_wait_time]
                    j+=1
        print(df)
        df.to_excel(excel_file, sheet_name='Sheet_name_1')
        # Use the 'hue' argument to provide a factor variable
        sns.catplot(data=df, x="Num_Floors", y="Passenger_Avg_Wait",
                        hue='System', kind='point',
                        legend='full',
                        palette={'Basic': 'dodgerblue', 'Improved': 'red'},
                        linestyles=["-", "--"], markers=["s", "d"])
        plt.title(str(num_people_sims[0]) + " Passengers - Lift Capacity " + str(capacity))
        plt.xlabel('Number of Floors')
        plt.ylabel('Average Wait Time Per Person')
        plt.show()