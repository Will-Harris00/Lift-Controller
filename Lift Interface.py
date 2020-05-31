from tkinter import *
from tkinter import messagebox


# self.master = Tk()

# entry class for setup


class root(Frame):
    def __init__(self, master):
        self.master = master

        self.canvas = Canvas(self.master, width=500, height=500, borderwidth=0,
                             highlightthickness=0, bg="lightblue")
        self.canvas.pack(fill="both", expand="true")
        self.numberOfFloors = 12

        self.redbutton = Button(self.master, text="Red", fg="red")
        self.redbutton.pack(side=LEFT)

        self.greenbutton = Button(self.master, text="green", fg="green")
        self.greenbutton.pack(side=LEFT)

        self.bluebutton = Button(self.master, text="Blue", fg="blue")
        self.bluebutton.pack(side=LEFT)
        self.canvas.update()

    def redraw(self, event=None):
        self.canvas.delete("lift")
        self.canvas.delete("shaft")
        self.canvas.delete("flrnums")
        self.canvas.delete("statusbar")
        self.statusbar = Label(self, anchor="sw")
        self.statusbar.configure(text="Number of floors: %s" % (self.numberOfFloors))
        self.frame = self.canvas.create_window(0, self.canvas.winfo_height(), window=self.statusbar,
                                               width=self.canvas.winfo_width(),
                                               height=self.statusbar.winfo_reqheight(), anchor="sw",
                                               tags="statusbar")
        self.lift = self.canvas.create_rectangle(self.canvas.winfo_width() / 2, 1,
                                                 self.canvas.winfo_width() - 3,
                                                 (
                                                             self.canvas.winfo_height() / self.numberOfFloors) - 1,
                                                 fill="pink", outline='grey', tags="lift")
        self.shaft = self.canvas.create_rectangle((self.canvas.winfo_width() / 2) - 1, 0,
                                                  self.canvas.winfo_width() - 2,
                                                  self.canvas.winfo_height() - (
                                                              self.statusbar.winfo_reqheight() + 2),
                                                  fill="white",
                                                  outline='black', width="1", tags="shaft")
        self.canvas.update()
        usable_height = self.canvas.winfo_height() - (15 + self.statusbar.winfo_height())
        start_low = self.canvas.winfo_height() - (self.statusbar.winfo_height())
        for i in range(self.numberOfFloors):
            # change the i at the end of the line to multiple -12 by either one or zero depending on if the floor number is zero or not
            # j = int(i > 0)
            self.floor_numbers = self.canvas.create_text(12, start_low - (
                        (i + 1) * (usable_height / (self.numberOfFloors))),
                                                         text=str(i), tags="flrnums",
                                                         font=('Arial', 12))
        # self.floor_numbers = self.canvas.create_text(12, -12 + (self.canvas.winfo_height() - self.statusbar.winfo_reqheight()) - (((i) * (self.canvas.winfo_height()/(self.numberOfFloors))) - (12 * j)), text=str(i), tags="flrnums", font=('Arial', 12))
        self.canvas.tag_raise(self.shaft)
        self.canvas.tag_raise(self.lift)


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

