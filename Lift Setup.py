from tkinter import *
from tkinter import messagebox
import random


class VarEntry(Frame):
    def __init__(self, root, numFloors=10, numPeople=50, liftCapacity=6):
        self.root = root

        self.error = StringVar()
        self.error.set('No errors currently detected.')
        self.errorLabel = Label(self.root, textvariable=self.error)
        self.errorLabel.pack(side="bottom", fill='both')

        self.floorsLabel = Label(self.root, text="Floors: ")
        self.floorsLabel.pack(side="left")
        self.inputNumFloors = Entry(self.root, textvariable="", width=3)
        self.inputNumFloors.pack(side="left")

        self.peopleLabel = Label(self.root, text="People: ")
        self.peopleLabel.pack(side="left", padx=4, pady=2)
        self.inputNumPeople = Entry(self.root, textvariable="", width=3)
        self.inputNumPeople.pack(side="left", pady=2)

        self.capacityLabel = Label(self.root, text="Lift Capacity: ")
        self.capacityLabel.pack(side="left", padx=4, pady=2)
        self.inputLiftCapacity = Entry(self.root, textvariable="", width=3)
        self.inputLiftCapacity.pack(side="left", pady=2)

        # set default values
        self.numFloors = numFloors
        self.numPeople = numPeople
        self.liftCapacity = liftCapacity
        self.inputNumFloors.insert(END, numFloors)
        self.inputNumPeople.insert(END, numPeople)
        self.inputLiftCapacity.insert(END, liftCapacity)
        # self.inputNumPeople.update()

        self.startBtn = Button(self.root, text="Run", fg="blue", width=5, command=self.validate)
        # command=lambda: self.validate()
        # self.startBtn.bind("<Button-1>", command=self.validate)
        self.root.bind("<Return>", lambda event: self.validate())
        self.startBtn.pack(side="right", padx=4, pady=2)
        self.root.title("Data Entry Form")
        self.root.resizable(False, False)
        # specifies position on screen with default window sizing
        self.root.geometry("+250+250")
        self.root.protocol("WM_DELETE_WINDOW", on_continue)
        self.root.mainloop()

        # self.liftTiles = {}
        # self.peopleList = []


    def validate(self):
        try:
            testFloors = int(self.inputNumFloors.get())
            try:
                testPeople = int(self.inputNumPeople.get())
                try:
                    testCapacity = int(self.inputLiftCapacity.get())
                    if testFloors < 2 or testFloors > 25:
                        self.error.set(
                            "The number of floors '" + str(testFloors) + "' is out of range. Please choose a number between 2 and 10.")
                        print(
                            "The number of floors '" + str(testFloors) + "' is out of range. Please choose a number between 2 and 10.")
                    elif testPeople < 1 or testPeople > 50:
                        self.error.set(
                            "The number of people '" + str(testPeople) + "' is out of range. Please choose a number between 1 and 50.")
                        print(
                            "The number of people '" + str(testPeople) + "' is out of range. Please choose a number between 1 and 50.")
                    elif testCapacity < 1 or testCapacity > 16:
                        self.error.set(
                            "The capacity of the lift '" + str(testCapacity) + "' is out of range. Please choose a number between 1 and 16.")
                        print(
                            "The capacity of the lift '" + str(testCapacity) + "' is out of range. Please choose a number between 1 and 16.")
                    else:
                        self.numFloors = testFloors
                        self.numPeople = testPeople
                        self.liftCapacity = testCapacity
                        # self.inputNumFloors.config(state="disabled")
                        # self.inputNumPeople.config(state="disabled")
                        # self.errorLabel.destroy()
                        # self.canvas.update()
                        # self.peopleLabel.config(text="P")
                        # self.floorsLabel.config(text="F")
                        self.root.destroy()
                except:
                    self.error.set("Please provide a valid input for lift capacity.")
            except:
                self.error.set("Please provide a valid input for number of people.")
        except:
            self.error.set("Please provide a valid input for number of floors.")


class Structure():
    def __init__(self, master):
        self.master = master

        self.canvas = Canvas(self.master, borderwidth=0, highlightthickness=0,
                             bg="lightblue")
        self.canvas.pack(fill="both", expand="true")
        self.canvas.delete("nums")
        self.canvas.delete("flrs")
        self.canvas.delete("divs")
        cellwidth = int(self.canvas.winfo_width() / 3)
        cellheight = int(round(self.canvas.winfo_height() / vars.numFloors))
        for column in range(3):
            current_floor = vars.numFloors
            if column in range(1, 3, 2):
                for row in range(vars.numFloors):
                    x1 = column * cellwidth
                    y1 = row * cellheight
                    x2 = x1 + cellwidth
                    y2 = y1 + cellheight
                    if row % 2 == 0:
                        y2 -= 1
                    self.canvas.create_line(0, y1, self.canvas.winfo_width(),
                                                      y1, fill="burlywood",
                                                      tags="divs")
                    liftPosition = self.canvas.create_rectangle(x1, y1, x2, y2,
                                                            fill="NavajoWhite",
                                                            tags="flrs")
                    lift.tiles[current_floor] = liftPosition
                    current_floor -= 1
            elif column in range(0, 3, 2):
                floor_num = 0
                for row in range(vars.numFloors, 0, -1):
                    y1 = (row * cellheight) - 5
                    if row % 2 == 0:
                        y1 -= 1
                    y2 = y1 - (cellheight // 1.5)
                    self.canvas.create_text(1, y2, anchor="nw", text=str(floor_num), tags="flrs",
                                            font=('Arial', -round(cellheight // 1.75)))
                    floor_num += 1
        """
        if self.inputNumFloors.get() and self.inputNumFloors.get() != "":
            self.inputNumFloors.config(state="disabled")
            self.inputNumPeople.config(state="disabled")
        """


class Building(object):
    def __init__(self):
        Building.move(self)


    def move(self):
        while len(peopleWaiting) > 0:
            # print("\nThe lift is on floor: " + str(lift.currentFloor))
            Building.collect(self)
            Building.deliver(self)
            lift.currentFloor += lift.direction
            lift.floorsMoved += 1
            if lift.currentFloor == numFloors - 1 or lift.currentFloor == 0:
                lift.direction *= -1


    def collect(self):
        for person in floorsList[lift.currentFloor].peopleOnFloor:
            # print("Person " + str(person.idPerson) + " is travelling in direction: " + str(person.direction) + " the lift direction is: " + str(lift.direction))
            # adds waiting passengers to the lift if travelling in the direction of the lift.
            if person.direction == lift.direction:
                People.destination(person)
                print("\nPerson " + str(person.idPerson) + " started on floor " +  str(person.originFlr) + " travelling in direction " + str(person.direction) + " to floor " + str(person.destFlr))
                # add as many passenger as possible before the lift becomes full.
                if len(lift.passengers) < lift.capacity:
                    lift.passengers.append(person)
                    floorsList[lift.currentFloor].peopleOnFloor.remove(person)
                    print("\nPerson " + str(person.idPerson) + " got in the lift at floor " + str(
                        lift.currentFloor))
                    print("There are " + str(len(lift.passengers)) + " passenger in the lift.")
                else:
                    break


    def deliver(self):
        for person in lift.passengers:
            if person.destFlr == lift.currentFloor:
                lift.passengers.remove(person)
                peopleArrived.append(person)
                peopleWaiting.remove(person)
                print("Person " + str(person.idPerson) + " got out of the lift on floor " + str(person.destFlr))
                print("There are " + str(len(lift.passengers)) + " passengers in the lift.")


class Lift(object):
    def __init__(self):
        self.capacity = vars.liftCapacity
        self.currentFloor = 0
        self.direction = 1
        self.floorsMoved = 0
        self.passengers = []
        self.tiles = {}


class People(object):
    def __init__(self, topFloor, personId):
        self.idPerson = personId
        self.flrsPassed = 0
        self.originFlr = random.randint(0, topFloor)

        if self.originFlr == topFloor:
            self.direction = -1
        elif self.originFlr == 0:
            self.direction = 1
        else:
            # randomly selects whether the passenger is travelling up or down
            self.direction = random.choice([-1, 1])
        # print("\n"+str(self.originFlr))
        # print(self.direction)
        # print(self.destFlr)


    def destination(self):
        # A destination floor is generated based on whether the passenger is
        # travelling up or down where only the applicable floors will be chosen.
        if self.direction == 1:
            # direction 1 shows the passenger wishes to travel to a higher floor
            selection = list(range(self.originFlr + 1, numFloors))
            self.direction = 1
        else:
            # direction -1 show the passenger wishes to travel to a lower floor
            selection = list(range(0, self.originFlr))
        self.destFlr = random.choice(selection)


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


def on_continue():
    if messagebox.askokcancel("Run animation", "Do you want to continue with default values?"):
        print("\nRunning simulation with default values.\n")
        root.destroy()


def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        master.destroy()


if __name__ == "__main__":
    # root is the entry window that validates the user input.
    root = Tk()
    # VarEntry is the class containing the user's input
    vars = VarEntry(root)
    # master is the animation window
    master = Tk()

    # creates the lift object and add the index of tiles to a dictionary
    lift = Lift()
    # Structure is the class containing the building objects
    structure = Structure(master)

    peopleWaiting = []
    peopleArrived = []
    floorsList = []
    numFloors = vars.numFloors
    numPeople = vars.numPeople

    for personId in range(0, numPeople):
        peopleWaiting.append(People(numFloors - 1, personId))
    # print(peopleWaiting)

    for floorId in range(0, numFloors):
        floorsList.append(Floors(peopleWaiting, floorId))
    # print(floorsList[numFloors - 1].idFloor)
    # print(floorsList[numFloors - 1].peopleOnFloor)

    Building()
    # print("The lift has travelled " + str(lift.floorsMoved) + " floors.")


    master.title("Lift Manager")
    master.protocol("WM_DELETE_WINDOW", on_closing)
    master.geometry("600x625+525+15")
    master.resizable(False, False)
    master.mainloop()



