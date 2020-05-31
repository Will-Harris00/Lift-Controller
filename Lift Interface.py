from tkinter import *
from tkinter import messagebox


class root(Frame):
    def __init__(self, master):
        self.master = master

        self.canvas = Canvas(self.master, width=500, height=500, borderwidth=0,
                             highlightthickness=0, bg="lightblue")
        self.canvas.pack(fill="both", expand="true")

        self.error = StringVar()
        self.errorLabel = Label(self.master, textvariable=self.error)
        self.error.set('No errors currently detected.')
        self.errorLabel.pack(side="bottom", fill='both')

        self.numFloors = IntVar()
        self.numPeople = IntVar()
        self.numFloors.set(10)
        self.numPeople.set(100)

        self.floorsString = StringVar()
        self.floorsString.set("Floors :")
        self.floorsLabel = Label(self.master, textvariable=self.floorsString)
        self.floorsLabel.pack(side="left")
        self.inputNumFloors = Entry(self.master, textvariable=self.numFloors, width=3)
        self.inputNumFloors.pack(side="left")

        self.peopleString = StringVar()
        self.peopleString.set("People :")
        self.peopleLabel = Label(self.master, textvariable=self.peopleString)
        self.peopleLabel.pack(side="left", padx=4, pady=2)
        self.inputNumPeople = Entry(self.master, textvariable=self.numPeople, width=3)
        self.inputNumPeople.pack(side="left", pady=2)

        self.info = StringVar()
        self.infoLabel = Label(self.master, textvariable=self.info)
        self.info.set('Information: ')
        self.infoLabel.pack(side="left", fill='both', padx=5, pady=2)

        self.startBtn = Button(self.master, text="Run", fg="green", width=5,
                               command=lambda: self.validate())
        self.startBtn.pack(side="right", padx=4, pady=2)
        self.autocompleteBtn = Button(self.master, text="Autocomplete", fg="blue")
        self.autocompleteBtn.pack(side="right", padx=4, pady=2)

    def validate(self):
        self.numFloors = int(self.inputNumFloors.get())
        self.numPeople = int(self.inputNumPeople.get())
        if self.numFloors < 2 or self.numFloors > 25:
            self.error.set(
                "The number of floors '" + self.inputNumPeople.get() + "' is out of range. Please choose a number between 2 and 30.")
            print(
                "The number of floors '" + self.inputNumPeople.get() + "' is out of range. Please choose a number between 2 and 30.")
        elif self.numPeople < 1 or self.numPeople > 200:
            self.error.set(
                "The number of people '" + self.inputNumFloors.get() + "' is out of range. Please choose a number between 1 and 200.")
            print(
                "The number of people '" + self.inputNumFloors.get() + "' is out of range. Please choose a number between 1 and 200.")
        else:
            self.inputNumFloors.config(state="disabled")
            self.inputNumPeople.config(state="disabled")
            self.error.set('No errors currently detected.')
            root.draw(self)

    def draw(self):
        self.canvas.create_rectangle(0, 0, 100, 100)


def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        master.destroy()


if __name__ == "__main__":
    master = Tk()
    master.title("Lift Manager")
    Frame = root(master)
    master.protocol("WM_DELETE_WINDOW", on_closing)
    master.minsize(350, 300)
    # root.pack_propagate(1)
    # root.update_idletasks()
    master.mainloop()

