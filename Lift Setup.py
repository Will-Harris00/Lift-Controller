from tkinter import *
from tkinter import messagebox
import random
import time


class VarEntry(Frame):
    def __init__(self, root, numFloors=10, numPeople=50, liftCapacity=6, **kw):
        super().__init__(**kw)
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

        # assign default values
        self.numFloors = numFloors
        self.numPeople = numPeople
        self.liftCapacity = liftCapacity
        self.inputNumFloors.insert(END, numFloors)
        self.inputNumPeople.insert(END, numPeople)
        self.inputLiftCapacity.insert(END, liftCapacity)

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
                    if testFloors < 2 or testFloors > 25:
                        self.error.set(
                            "The number of floors '" + str(
                                testFloors) + "' is out of range. Please choose a number between 2 and 10.")
                        print(
                            "The number of floors '" + str(
                                testFloors) + "' is out of range. Please choose a number between 2 and 10.")
                    elif testPeople < 1 or testPeople > 50:
                        self.error.set(
                            "The number of people '" + str(
                                testPeople) + "' is out of range. Please choose a number between 1 and 50.")
                        print(
                            "The number of people '" + str(
                                testPeople) + "' is out of range. Please choose a number between 1 and 50.")
                    elif testCapacity < 1 or testCapacity > 16:
                        self.error.set(
                            "The capacity of the lift '" + str(
                                testCapacity) + "' is out of range. Please choose a number between 1 and 16.")
                        print(
                            "The capacity of the lift '" + str(
                                testCapacity) + "' is out of range. Please choose a number between 1 and 16.")
                    else:
                        self.numFloors = testFloors
                        self.numPeople = testPeople
                        self.liftCapacity = testCapacity
                        self.root.destroy()
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
        self.canvas = Canvas(self.master, width=500, height=500, borderwidth=0,
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
                    line = self.canvas.create_line(0, y1, self.canvas.winfo_reqwidth(),
                                            y1, fill="BurlyWood",
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
                        departed_num = self.canvas.create_text(cellwidth - 3, y2 + 3, anchor="ne",
                                                text=str(len(waiting[floor_num])),
                                                fill="CadetBlue",
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
                                                fill="CadetBlue",
                                                font=('Arial', -round(cellheight // 2)))
                        self.arrivals[floor_num] = arrived_num
                        # print("Arrive number: " + str(arrived_num))
                    floor_num += 1
        # print(lift.tiles)
        # print(self.departures)
        # print(self.arrivals)
        self.master.title("Lift Manager")
        self.master.protocol("WM_DELETE_WINDOW", on_closing)
        self.master.geometry("500x525+350+75")
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
        Building.move(self)

    def move(self):
        while len(waiting) > 0 or len(lift.passengers) > 0:
            print("\nThe lift is on floor: " + str(lift.currentFloor))
            if not ((lift.currentFloor == numFloors - 1) or (lift.currentFloor == 0)):
                try:
                    tile = lift.tiles[lift.currentFloor - lift.direction]
                    model.canvas.itemconfigure(tile, fill="NavajoWhite")
                    model.canvas.update()
                except KeyError:
                    pass
            else:
                tile = lift.tiles[lift.currentFloor + lift.direction]
                model.canvas.itemconfigure(tile, fill="NavajoWhite")
                model.canvas.update()
            # people are delivered before collecting others on the same floor
            # to ensure optimal transportation as they must be travelling to
            # a floor different from their origin, this frees up lift space.
            Building.deliver(self)
            Building.collect(self)
            tile = lift.tiles[lift.currentFloor]
            model.canvas.itemconfigure(tile, fill="LightPink")
            model.canvas.update()
            lift.currentFloor += lift.direction
            lift.floorsMoved += 1
            # Model.update(self, numRemaining)
            if lift.currentFloor == numFloors - 1 or lift.currentFloor == 0:
                lift.direction *= -1
            time.sleep(0.1)
        model.master.mainloop()


    def collect(self):
        try:
            for person in waiting[lift.currentFloor]:
                # print("Person " + str(person.idPerson) + " is travelling in direction: " + str(person.direction) + " the lift direction is: " + str(lift.direction))
                # adds waiting passengers to the lift if travelling in the direction of the lift.
                if person.direction == lift.direction:
                    People.destination(person)
                    # print("\nPerson " + str(person.idPerson) + " started on floor " +  str(person.originFlr) + " travelling in direction " + str(person.direction) + " to floor " + str(person.destFlr))
                    # add as many passenger as possible before the lift becomes full.
                    if len(lift.passengers) < lift.capacity:
                        lift.passengers.append(person)
                        waiting[lift.currentFloor].remove(person)
                        # change the value of people waiting on that floor
                        departed_num = model.departures[lift.currentFloor]
                        model.canvas.itemconfigure(departed_num, text=str(len(waiting[lift.currentFloor])))
                        model.canvas.update()
                        if len(waiting[lift.currentFloor]) == 0:
                            del waiting[lift.currentFloor]
                        print("\nPerson " + str(person.id) + " got in the lift at floor " + str(lift.currentFloor))
                        print("There are " + str(len(lift.passengers)) + " passenger in the lift.")
                    # saves searching through the remaining passengers if the lift is already full.
                    else:
                        break
        except:
            pass

    def deliver(self):
        for person in lift.passengers:
            if person.destFlr == lift.currentFloor:
                if person.destFlr not in delivered:
                    delivered[person.destFlr] = []
                delivered[person.destFlr].append(person)
                lift.passengers.remove(person)
                # change the value of people having arrived on that floor.
                arrive_num = model.arrivals[lift.currentFloor]
                model.canvas.itemconfigure(arrive_num, text=str(len(delivered[lift.currentFloor])))
                model.canvas.update()
                print("Person " + str(person.id) + " exited the lift on floor " + str(person.destFlr))
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
    # master is the animation window
    master = Tk()
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

    # Model is the class containing the building objects
    model = Model(master)

    Building()
    # print("The lift has travelled " + str(lift.floorsMoved) + " floors.")
