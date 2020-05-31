import tkinter
import time
from tkinter import messagebox


class root(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Lift Manager")
        self.canvas = tkinter.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0, closeenough=0, relief='ridge', bg="lightblue")
        self.numberOfFloors = 10
        self.canvas.pack(side="top", fill="both", expand="true")
        self.canvas.bind("<Configure>", self.redraw)

    def redraw(self, event=None):
        self.canvas.delete("lift")
        self.canvas.delete("shaft")
        self.lift = self.canvas.create_rectangle(self.canvas.winfo_reqwidth() / 2, 1,
                                                 self.canvas.winfo_reqwidth() - 3,
                                                 (self.canvas.winfo_reqheight() / self.numberOfFloors) - 1,
                                                 fill="pink", outline='grey', tags="lift")
        self.shaft = self.canvas.create_rectangle((self.canvas.winfo_reqwidth() / 2) - 1, 0,
                                                  self.canvas.winfo_reqwidth() - 2,
                                                  self.canvas.winfo_reqheight() - 2, fill="white",
                                                  outline='black', width="1", tags="shaft")
        self.canvas.tag_raise(self.shaft)
        self.canvas.tag_raise(self.lift)
        self.status = tkinter.Label(self, anchor="sw")
        self.status.pack(side="bottom", fill="x")
        self.status.pack_propagate(1)
        self.status.configure(text="Number of floors: %s" % (self.numberOfFloors))

    def move(self):
        xspeed = 0
        yspeed = 1
        while True:
            self.canvas.move(self.lift, xspeed, yspeed)
            position = self.canvas.coords(self.lift)
            self.root.update()
            self.canvas.update()
            time.sleep(0.02)
            if position[3] >= 500:
                yspeed = -yspeed
            elif position[1] == 500:
                yspeed = -yspeed

def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        root.destroy()

if __name__ == "__main__":
    root = root()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.minsize(350, 300)
    root.pack_propagate(1)
    root.update_idletasks()
    root.mainloop()

