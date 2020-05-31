from tkinter import *
from tkinter import messagebox
import random


class model(Frame):
    def __init__(self, root):
        self.root = root

        self.canvas = Canvas(self.root, width=500, height=500, borderwidth=0, highlightthickness=0,
                             bg="lightblue")
        self.canvas.pack(fill="both", expand="true")

        self.error = StringVar()
        self.error.set('No errors currently detected.')
        self.errorLabel = Label(self.root, textvariable=self.error)
        self.errorLabel.pack(side="bottom", fill='both')

        self.floorsLabel = Label(self.root, text="Storeys: ")
        self.floorsLabel.pack(side="left")
        self.inputNumFloors = Entry(self.root, textvariable="100", width=3)
        self.inputNumFloors.pack(side="left")

        self.peopleLabel = Label(self.root, text="People: ")
        self.peopleLabel.pack(side="left", padx=4, pady=2)
        self.inputNumPeople = Entry(self.root, textvariable="10", width=3)
        self.inputNumPeople.pack(side="left", pady=2)

        self.info = StringVar()
        self.infoLabel = Label(self.root, textvariable=self.info)
        self.info.set('Information: ')
        self.infoLabel.pack(side="left", fill='both', padx=5, pady=2)

        self.startBtn = Button(self.root, text="Run", fg="green", width=5,
                               command=lambda: self.validate())
        self.startBtn.pack(side="right", padx=4, pady=2)
        self.autocompleteBtn = Button(self.root, text="Autocomplete", fg="blue")
        self.autocompleteBtn.pack(side="right", padx=4, pady=2)
        self.liftTiles = {}
        self.peopleList = []

    def validate(self):
        self.numFloors = int(self.inputNumFloors.get())
        self.numPeople = int(self.inputNumPeople.get())
        if self.numFloors < 2 or self.numFloors > 25:
            self.error.set(
                "The number of floors '" + self.inputNumFloors.get() + "' is out of range. Please choose a number between 2 and 10.")
            print(
                "The number of floors '" + self.inputNumFloors.get() + "' is out of range. Please choose a number between 2 and 10.")
        elif self.numPeople < 1 or self.numPeople > 50:
            self.error.set(
                "The number of people '" + self.inputNumPeople.get() + "' is out of range. Please choose a number between 1 and 50.")
            print(
                "The number of people '" + self.inputNumPeople.get() + "' is out of range. Please choose a number between 1 and 50.")
        else:
            # self.inputNumFloors.config(state="disabled")
            # self.inputNumPeople.config(state="disabled")
            self.error.set('No errors currently detected.')
            model.draw()

        tile = self.liftTiles[3]
        tile_color = self.canvas.itemcget(tile, "fill")
        new_color = "pink" if tile_color == "NavajoWhite" else "pink"
        self.canvas.itemconfigure(tile, fill=new_color)

    def draw(self):
        self.canvas.delete("nums")
        self.canvas.delete("flrs")
        self.canvas.delete("divs")
        cellwidth = int(self.canvas.winfo_width() / 3)
        cellheight = int(round(self.canvas.winfo_height() / self.numFloors))
        for column in range(3):
            current_floor = self.numFloors
            if column in range(1, 3, 2):
                for row in range(self.numFloors):
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
                    self.liftTiles[current_floor] = liftPosition
                    current_floor -= 1
            elif column in range(0, 3, 2):
                floor_num = 0
                for row in range(self.numFloors + 1, 0, -1):
                    y1 = (row * cellheight) - 5
                    if row % 2 == 0:
                        y1 -= 1
                    y2 = y1 - (cellheight // 1.5)
                    self.canvas.create_text(1, y2, anchor="nw", text=str(floor_num), tags="flrs",
                                            font=('Arial', -round(cellheight // 1.75)))
                    floor_num += 1
        model.genPeople()

    def genPeople(self):
        for i in range(1, self.numPeople + 1):
            self.peopleList.append(people(self.numFloors))
        print(self.peopleList)
        print(self.liftTiles)


class people(object):
    def __init__(self, numFloors):
        selection = []
        start = random.randint(0, numFloors)
        selection += (list(range(0, start)))
        selection += (list(range(start + 1, numFloors + 1)))
        end = random.choice(selection)
        if end > start:
            self.direction = "UP"
        else:
            self.direction = "DOWN"
        self.originFlr = start
        self.destFlr = end
        print("\n" + str(self.originFlr))
        print(self.direction)
        print(self.destFlr)


class elevator(object):
    def __init__(self, root):
        self.capacity = 6
        self.floor = 1
        self.direction = "UP"
        # elevator.move(self, 1)

    """
    def move(self, position):
        print(root)
        tile = root.liftTiles[position]
        tile_color = root.canvas.itemcget(tile, "fill")
        new_color = "pink" if tile_color == "NavajoWhite" else "pink"
        root.canvas.itemconfigure(tile, fill=new_color)
    """


def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Lift Manager")

    model = model(root)
    lift = elevator(root)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.geometry("600x625+525+15")
    root.resizable(False, False)

    # root.pack_propagate(1)
    # root.update_idletasks()
    root.mainloop()