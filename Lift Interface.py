from tkinter import *
from tkinter import messagebox


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

        # self.numFloors = IntVar(value=10)
        # self.numPeople = IntVar(value=100)

        self.floorsLabel = Label(self.root, text="Floors :")
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

    def validate(self):
        self.numFloors = int(self.inputNumFloors.get())
        self.numPeople = int(self.inputNumPeople.get())
        if self.numFloors < 2 or self.numFloors >= 25:
            self.error.set(
                "The number of floors '" + self.inputNumPeople.get() + "' is out of range. Please choose a number between 2 and 25.")
            print(
                "The number of floors '" + self.inputNumPeople.get() + "' is out of range. Please choose a number between 2 and 25.")
        elif self.numPeople < 1 or self.numPeople >= 200:
            self.error.set(
                "The number of people '" + self.inputNumFloors.get() + "' is out of range. Please choose a number between 1 and 200.")
            print(
                "The number of people '" + self.inputNumFloors.get() + "' is out of range. Please choose a number between 1 and 200.")
        else:
            self.inputNumFloors.config(state="disabled")
            self.inputNumPeople.config(state="disabled")
            self.error.set('No errors currently detected.')
            model.draw()

    def draw(self):
        for i in range(self.numFloors):
            self.canvas.create_line(0, self.canvas.winfo_height() / self.numFloors * i + 1,
                                    self.canvas.winfo_width(),
                                    self.canvas.winfo_height() / self.numFloors * i + 1,
                                    fill="burlywood", width=2)


def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Lift Manager")
    model = model(root)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.geometry("600x625+525+15")
    root.resizable(False, False)

    # root.pack_propagate(1)
    # root.update_idletasks()
    root.mainloop()

