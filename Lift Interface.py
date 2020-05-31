from tkinter import *
from tkinter import messagebox


class model(Frame):
    def __init__(self, master):
        self.master = master

        self.canvas = Canvas(self.master, width=500, height=500, borderwidth=0, highlightthickness=0,
                             bg="lightblue")
        self.canvas.pack(fill="both", expand="true")

        self.error = StringVar()
        self.error.set('No errors currently detected.')
        self.errorLabel = Label(self.master, textvariable=self.error)
        self.errorLabel.pack(side="bottom", fill='both')

        self.floorsLabel = Label(self.master, text="Floors: ")
        self.floorsLabel.pack(side="left")
        self.inputNumFloors = Entry(self.master, textvariable="", width=3)
        self.inputNumFloors.pack(side="left")

        self.peopleLabel = Label(self.master, text="People: ")
        self.peopleLabel.pack(side="left", padx=4, pady=2)
        self.inputNumPeople = Entry(self.master, textvariable="", width=3)
        self.inputNumPeople.pack(side="left", pady=2)

        self.info = StringVar()
        self.infoLabel = Label(self.master, textvariable=self.info)
        self.info.set('Information: ')
        self.infoLabel.pack(side="left", fill='both', padx=5, pady=2)

        self.startBtn = Button(self.master, text="Run", fg="green", width=5)
        #command=lambda: self.validate()
        self.startBtn.bind("<Button-1>", lambda event : self.validate())
        self.startBtn.pack(side="right", padx=4, pady=2)
        self.autocompleteBtn = Button(self.master, text="Autocomplete", fg="blue")
        self.autocompleteBtn.pack(side="right", padx=4, pady=2)

        self.liftTiles = {}
        self.peopleList = []


    def validate(self):
        try:
            self.numFloors = int(self.inputNumFloors.get())
            try:
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
                    self.errorLabel.destroy()
                    self.canvas.update()
                    self.peopleLabel.config(text="P")
                    self.floorsLabel.config(text="F")
                    model.draw()
            except:
                self.error.set("Please provide a valid input for number of people.")
        except:
            self.error.set("Please provide a valid input for number of floors.")


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
                for row in range(self.numFloors, 0, -1):
                    y1 = (row * cellheight) - 5
                    if row % 2 == 0:
                        y1 -= 1
                    y2 = y1 - (cellheight // 1.5)
                    self.canvas.create_text(1, y2, anchor="nw", text=str(floor_num), tags="flrs",
                                            font=('Arial', -round(cellheight // 1.75)))
                    floor_num += 1

        if self.inputNumFloors.get() and self.inputNumFloors.get() != "":
            self.inputNumFloors.config(state="disabled")
            self.inputNumPeople.config(state="disabled")

def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        master.destroy()


if __name__ == "__main__":
    master = Tk()
    master.title("Lift Manager")
    model = model(master)
    #peopleList = p.genPeople(model.numPeople, model.numFloors)

    master.protocol("WM_DELETE_WINDOW", on_closing)
    master.geometry("600x625+525+15")
    master.resizable(False, False)
    master.mainloop()