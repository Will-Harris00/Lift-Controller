from tkinter import *
from tkinter import messagebox
import random
import time


class VarEntry(Frame):
    def __init__(self, root, numFloors=10, numPeople=50, liftCapacity=6, numRepeats=1, delay=0.35, **kw):
        super().__init__(**kw)
        self.root = root

        self.error = StringVar()
        self.error.set('If the number of repeats if greater that 1 then the animation will be turned off.')
        self.errorLabel = Label(self.root, textvariable=self.error)
        self.errorLabel.pack(side="bottom", fill='both')

        # radio button selector to choose system logic.
        self.systemLogic = BooleanVar()
        self.systemLabel = Label(self.root, text="System logic: ")
        self.systemLabel.pack(side="left", padx=4, pady=2)
        self.inputSystem = Radiobutton(self.root, text="Improved", variable=self.systemLogic, value=False).pack(side="left")
        self.inputSystem = Radiobutton(self.root, text="Basic", variable=self.systemLogic, value=True).pack(side="left")

        self.floorsLabel = Label(self.root, text="Floors: ")
        self.floorsLabel.pack(side="left")
        self.inputNumFloors = Entry(self.root, textvariable="", width=5)
        self.inputNumFloors.pack(side="left")

        self.peopleLabel = Label(self.root, text="People: ")
        self.peopleLabel.pack(side="left", padx=4, pady=2)
        self.inputNumPeople = Entry(self.root, textvariable="", width=8)
        self.inputNumPeople.pack(side="left", pady=2)

        self.capacityLabel = Label(self.root, text="Lift Capacity: ")
        self.capacityLabel.pack(side="left", padx=4, pady=2)
        self.inputLiftCapacity = Entry(self.root, textvariable="", width=3)
        self.inputLiftCapacity.pack(side="left", pady=2)

        self.repeatsLabel = Label(self.root, text="Num Repeats: ")
        self.repeatsLabel.pack(side="left", padx=4, pady=2)
        self.inputNumRepeats = Entry(self.root, textvariable="", width=4)
        self.inputNumRepeats.pack(side="left", pady=2)

        self.delayLabel = Label(self.root, text="Delay Secs: ")
        self.delayLabel.pack(side="left", padx=4, pady=2)
        self.inputDelay = Entry(self.root, textvariable="", width=4)
        self.inputDelay.pack(side="left", pady=2)

        # assign default values
        self.numFloors = numFloors
        self.numPeople = numPeople
        self.liftCapacity = liftCapacity
        self.numRepeats = numRepeats
        self.delay = delay
        self.animate = True
        self.inputNumFloors.insert(END, numFloors)
        self.inputNumPeople.insert(END, numPeople)
        self.inputLiftCapacity.insert(END, liftCapacity)
        self.inputNumRepeats.insert(END, numRepeats)
        self.inputDelay.insert(END, delay)

        # bind left click on run bottom to validation of user input.
        self.startBtn = Button(self.root, text="Run", fg="blue", width=5, command=self.validate)
        self.startBtn.pack(side="right", padx=4, pady=2)

        # alternatively binds enter/return key to validation of user input.
        self.root.bind("<Return>", lambda event: self.validate())

        # sets window title.
        self.root.title("Data Entry Form")
        # disables resizing of window, defaults to minimum size required to fit all elements.
        self.root.resizable(False, False)
        # specifies position on screen with default window sizing.
        self.root.geometry("+250+250")
        # defines exit protocol when clicking the red x button to close the program.
        self.root.protocol("WM_DELETE_WINDOW", on_continue)
        # continuously check for any updates made to the window and canvas.
        self.root.mainloop()

    def validate(self):
        try:
            testFloors = int(self.inputNumFloors.get())
            try:
                testPeople = int(self.inputNumPeople.get())
                try:
                    testCapacity = int(self.inputLiftCapacity.get())
                    try:
                        testRepeats = int(self.inputNumRepeats.get())
                        try:
                            testDelay = float(self.inputDelay.get())
                            if testFloors < 2:
                                self.error.set(
                                    "The number of floors '" + str(
                                        testFloors) + "' is out of range. Please choose a number greater that 1.")
                                print(
                                    "The number of floors '" + str(
                                        testFloors) + "' is out of range. Please choose a number greater than 1.")
                            elif testPeople < 1:
                                self.error.set(
                                    "The number of people '" + str(
                                        testPeople) + "' is out of range. Please choose a number greater than 0.")
                                print(
                                    "The number of people '" + str(
                                        testPeople) + "' is out of range. Please choose a number greater than 0.")
                            elif testCapacity < 1 or testCapacity > 16:
                                self.error.set(
                                    "The capacity of the lift '" + str(
                                        testCapacity) + "' is out of range. Please choose a number greater than 0.")
                                print(
                                    "The capacity of the lift '" + str(
                                        testCapacity) + "' is out of range. Please choose a number greater than 0.")
                            elif testRepeats < 1 or testRepeats > 1000:
                                self.error.set(
                                    "The number of repeats '" + str(
                                        testRepeats) + "' is out of range. Please choose a number between 1 and 1000.")
                                print(
                                    "The number of repeats '" + str(
                                        testRepeats) + "' is out of range. Please choose a number between 1 and 1000.")
                            elif testDelay < 0 or testDelay > 2:
                                self.error.set(
                                    "The animation delay '" + str(
                                        testDelay) + "' is out of range. Please choose a number between 0 and 2 seconds.")
                                print(
                                    "The animation delay '" + str(
                                        testDelay) + "' is out of range. Please choose a number between 0 and 2 seconds.")
                            else:
                                self.numFloors = testFloors
                                self.numPeople = testPeople
                                self.liftCapacity = testCapacity
                                self.numRepeats = testRepeats
                                self.delay = testDelay
                                self.systemLogic = self.systemLogic.get()
                                if self.systemLogic:
                                    print("Basic system")
                                else:
                                    print("Improved system")
                                print("Number of floors: " +str(self.numFloors))
                                print("Number of people: " +str(self.numPeople))
                                print("Lift capacity: " +str(self.liftCapacity))
                                print("Number of repetitions: " + str(self.numRepeats -1))
                                print("Number of floors: " +str(self.numFloors))
                                if self.numRepeats == 1:
                                    self.animate = True
                                    print("Animation delay: " + str(self.delay))
                                else:
                                    self.animate = False
                                    print("Animated: " + str(self.animate))
                                self.root.destroy()
                        except:
                            self.error.set("Please provide a valid input for animation delay.")
                    except:
                        self.error.set("Please provide a valid input for number of repeats.")
                except:
                    self.error.set("Please provide a valid input for lift capacity.")
            except:
                self.error.set("Please provide a valid input for number of people.")
        except:
            self.error.set("Please provide a valid input for number of floors.")


class Model():
    def __init__(self, master):
        self.departures = {}
        self.arrivals = {}
        self.master = master
        self.canvas = Canvas(self.master, width=master.winfo_screenwidth()-20, height=master.winfo_screenheight()-125, borderwidth=0,
                             highlightthickness=0,
                             bg="lightblue")
        self.canvas.pack(fill="both", expand="true")

        self.canvas.delete("nums")
        self.canvas.delete("flrs")
        self.canvas.delete("divs")
        cellwidth = int(self.canvas.winfo_reqwidth() / 3)
        cellheight = int(round(self.canvas.winfo_reqheight() / vars.numFloors))
        for column in range(3):
            current_floor = vars.numFloors
            if column == 1:
                for row in range(vars.numFloors):
                    x1 = column * cellwidth
                    y1 = row * cellheight
                    x2 = x1 + cellwidth
                    y2 = y1 + cellheight
                    if row % 2 == 0:
                        y2 -= 1
                    line = self.canvas.create_line(0, y1, self.canvas.winfo_reqwidth(), y1,
                                                   fill="BurlyWood",
                                                   tags="divs")
                    # print("Line divider: " + str(line))
                    tile = self.canvas.create_rectangle(x1, y1, x2, y2,
                                                        fill="NavajoWhite",
                                                        tags="flrs")
                    # print("Lift Tile: " + str(tile))
                    lift.tiles[current_floor - 1] = tile
                    current_floor -= 1
            elif column in range(0, 3, 2):
                floor_num = 0
                for row in range(vars.numFloors, 0, -1):
                    if column == 0:
                        y1 = (row * cellheight) - 5
                        if row % 2 == 0:
                            y1 -= 1
                        y2 = y1 - (cellheight // 1.5)
                        num = self.canvas.create_text(1, y2, anchor="nw", text=str(floor_num), tags="flrs",
                                                font=('Arial', -round(cellheight // 1.75)))
                        # print("Floor number: " + str(num))
                        try:
                            num_waiting = len(waiting[floor_num])
                        except KeyError:
                            num_waiting =  0
                        departed_num = self.canvas.create_text(cellwidth - 3, y2 + 3, anchor="ne",
                                                text=str(num_waiting),
                                                fill="Crimson",
                                                font=('Arial', -round(cellheight // 2)))
                        self.departures[floor_num] = departed_num
                        # print("Depart number: " + str(departed_num))
                    elif column == 2:
                        y1 = (row * cellheight) - 5
                        if row % 2 == 0:
                            y1 -= 1
                        y2 = y1 - (cellheight // 1.5)
                        arrived_num = self.canvas.create_text((cellwidth * column) + 3, y2 + 3, anchor="nw",
                                                text="0",
                                                fill="DodgerBlue",
                                                font=('Arial', -round(cellheight // 2)))
                        self.arrivals[floor_num] = arrived_num
                        # print("Arrive number: " + str(arrived_num))
                    floor_num += 1
        # print(lift.tiles)
        # print(self.departures)
        # print(self.arrivals)
        self.master.title("Lift Manager")
        self.master.protocol("WM_DELETE_WINDOW", on_closing)
        string_geometry = str(master.winfo_screenwidth()-20)+"x"+str(master.winfo_screenheight()-75)+"+0+0"
        print("Window geometry: " + string_geometry)
        self.master.geometry(string_geometry)
        self.master.resizable(False, False)
        self.master.update()

    """
    def update(self, numRemaining):
        self.peopleRemaining = Label(self.master, text="People remaining: " + str(numRemaining))
        self.peopleRemaining.pack(side="left")
        self.floorsMoved = Label(self.master, text="Floors moved: " + str(
            lift.floorsMoved))
        self.floorsMoved.pack(side="left")
        self.master.update()
    """


class Building(object):
    def __init__(self):
        self.peopleDelivered = 0
        Building.move(self)

    def move(self):
        self.all_delivered = False
        print("\nThe lift is on floor: 0")
        while len(waiting) > 0 or len(lift.passengers) > 0:
            if self.all_delivered == False:

                if vars.animate == True:
                    tile = lift.tiles[lift.currentFloor]
                    model.canvas.itemconfigure(tile, fill="Pink")
                    model.canvas.update()
                    time.sleep(vars.delay)

                # people are delivered before collecting others on the same floor
                # to ensure optimal transportation as they must be travelling to
                # a floor different from their origin, this frees up lift space.
                Building.deliver(self)
                Building.travel(self)
                Building.collect(self)

                if vars.animate == True:
                    tile = lift.tiles[lift.currentFloor]
                    model.canvas.itemconfigure(tile, fill="NavajoWhite")
                    model.canvas.update()
                    fin_position = lift.currentFloor
            else:
                break
        # need to remove the one extra move counted
        # because the while loop runs to completion.
        lift.floorsMoved -= 1
        print("\nThe lift travelled: " + str(lift.floorsMoved) + " floors in total.")
        print("The average number of floors traversed to deliver each passenger is " + str(lift.floorsMoved/numPeople))

        if vars.animate == True:
            # display the final floor the list ends on.
            tile = lift.tiles[fin_position]
            model.canvas.itemconfigure(tile, fill="Pink")
            model.canvas.update()
            model.master.mainloop()


    def collect(self):
        try:
            for person in waiting[lift.currentFloor][:]:
                # print("Person " + str(person.id) + " is travelling in direction: " + str(person.direction) + " the lift direction is: " + str(lift.direction))
                # adds waiting passengers to the lift if travelling in the direction of the lift.
                    People.destination(person)
                    # print("\nPerson: " + str(person.id) + " started on floor " +  str(person.originFlr) + " travelling in direction " + str(person.direction) + " to floor " + str(person.destFlr))
                    # add as many passenger as possible before the lift becomes full.
                    if len(lift.passengers) < lift.capacity:
                        lift.passengers.append(person)

                        if vars.animate == True:
                            tile = lift.tiles[lift.currentFloor]
                            model.canvas.itemconfigure(tile, fill="ForestGreen")
                            model.canvas.update()
                            time.sleep(vars.delay/5)
                            model.canvas.itemconfigure(tile, fill="Pink")
                            model.canvas.update()

                        waiting[lift.currentFloor].remove(person)

                        if vars.animate == True:
                            # change the value of people waiting on that floor
                            departed_num = model.departures[lift.currentFloor]
                            model.canvas.itemconfigure(departed_num, text=str(len(waiting[lift.currentFloor])))
                            model.canvas.update()
                            time.sleep(vars.delay/2)

                        if len(waiting[lift.currentFloor]) == 0:
                            del waiting[lift.currentFloor]
                        print("\nPerson " + str(person.id) + " got in the lift at floor " + str(lift.currentFloor))
                        print("There are " + str(len(lift.passengers)) + " passenger in the lift.")
                    # saves searching through the remaining waiting passengers if the lift is already full.
                    else:
                        break
        except:
            if len(waiting) == 0:
                self.all_delivered = True
            else:
                num_on_floor = []
                floors_index = []
                # count the number of people on each floor to determine where to go next
                for floor in waiting:
                    num_on_floor.append(len(waiting[floor]))
                    floors_index.append(floor)
                    print("\nFloor " + str(floor) + " has " + str(len(waiting[floor])) + " people waiting.")

                # finds the floor with the greatest number of people waiting
                next_floor = floors_index[num_on_floor.index(max(num_on_floor))]

                print(num_on_floor)
                print("\nThe next floor to go to is floor " + str(next_floor) +" with " + str(max(num_on_floor)) + " people waiting.")
                print("\nThe lift travelled: " + str(lift.floorsMoved) + " floors in total.")
                print("The number of people delivered is: " + str(self.peopleDelivered))
                print("The average number of floors traversed to deliver each passenger is " + str(
                    lift.floorsMoved / self.peopleDelivered))


                # collection algorithm goes here
                # closest floor with priority of greatest number waiting
                flrs_difference = next_floor - lift.currentFloor

                for i in range(abs(flrs_difference)):
                    if flrs_difference > 0:
                        lift.currentFloor += 1
                        print("\nThe lift is on floor: " + str(lift.currentFloor))
                    else:
                        lift.currentFloor -= 1
                        print("\nThe lift is on floor: " + str(lift.currentFloor))
                    lift.floorsMoved += 1
                pass

    def deliver(self):
        self.travel()
        for person in lift.passengers[:]:
            if person.destFlr == lift.currentFloor:
                if person.destFlr not in delivered:
                    delivered[person.destFlr] = []
                delivered[person.destFlr].append(person)

                if vars.animate == True:
                    tile = lift.tiles[lift.currentFloor]
                    model.canvas.itemconfigure(tile, fill="Orange")
                    model.canvas.update()
                    time.sleep(vars.delay/5)
                    model.canvas.itemconfigure(tile, fill="Pink")
                    model.canvas.update()
                self.peopleDelivered+=1
                lift.passengers.remove(person)

                if vars.animate == True:
                    # change the value of people having arrived on that floor.
                    arrive_num = model.arrivals[lift.currentFloor]
                    model.canvas.itemconfigure(arrive_num, text=str(len(delivered[lift.currentFloor])))
                    model.canvas.update()
                    time.sleep(vars.delay/2)

                print("Person " + str(person.id) + " exited the lift on floor " + str(person.destFlr))
                print("There are " + str(len(lift.passengers)) + " passengers in the lift.")

    def travel(self):
        real_diffs = []
        for person in lift.passengers:
            dest_difference = person.destFlr - lift.currentFloor
            real_diffs.append(dest_difference)

        # finds the difference to the next closest floor for delivery
        try:
            min_abs_value = abs(real_diffs[0])
            min_real_value = real_diffs[0]
            for num in real_diffs:
                if abs(num) < min_abs_value:
                    min_abs_value = abs(num)
                    min_real_value = num

            for i in range(abs(min_real_value)):
                # Moves the lift up or down depending on the direction.
                if min_real_value > 0:
                    lift.currentFloor += 1
                    print("\nThe lift is on floor: " + str(lift.currentFloor))
                else:
                    lift.currentFloor -= 1
                    print("\nThe lift is on floor: " + str(lift.currentFloor))
                lift.floorsMoved += 1

        # there was nobody in the lift
        except:
            pass



class Lift(object):
    def __init__(self):
        self.capacity = vars.liftCapacity
        self.currentFloor = 0
        self.direction = 1
        self.floorsMoved = 0
        self.passengers = []
        self.tiles = {}


class People(object):
    def __init__(self, topFloor, id):
        self.id = id
        self.flrsPassed = 0
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


def assign(person):
    if person.originFlr not in waiting:
        waiting[person.originFlr] = []
    waiting[person.originFlr].append(person)


"""
class Floors(object):
    def __init__(self, peopleWaiting, floorId):
        self.idFloor = floorId
        self.count = 0
        self.peopleOnFloor = Floors.assign(self, peopleWaiting)
        print("Floor " + str(self.idFloor) + " has " + str(
            len(self.peopleOnFloor)) + " passengers waiting.")

    def assign(self, peopleWaiting):
        self.peopleOnFloor = []
        for k in peopleWaiting:
            if k.originFlr == floorId:
                self.peopleOnFloor.append(k)
        return self.peopleOnFloor
"""

def on_continue():
    if messagebox.askokcancel("Run animation", "Do you want to continue with default values?"):
        print("\nRunning simulation with default values.\n")
        root.destroy()


def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        Building.wait = 0
        master.destroy()


if __name__ == "__main__":
    # root is the entry window that validates the user input.
    root = Tk()
    # VarEntry is the class containing the user's input
    vars = VarEntry(root)

    if vars.animate == True:
        # master is the animation window
        master = Tk()

    while vars.numRepeats > 0:
        print("\nSimulation number: " + str(vars.numRepeats))
        # creates the lift object and add the index of tiles to a dictionary
        lift = Lift()

        waiting = {}
        delivered = {}
        # floorsList = []
        numFloors = vars.numFloors
        numPeople = vars.numPeople

        for id in range(0, numPeople):
            person = (People(numFloors - 1, id))
            assign(person)
        print(waiting)
        # print(peopleWaiting)

        if vars.animate == True:
            # Model is the class containing the building objects
            model = Model(master)

        Building()
        # print("The lift has travelled " + str(lift.floorsMoved) + " floors.")

        vars.numRepeats -= 1
