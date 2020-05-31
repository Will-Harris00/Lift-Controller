import tkinter
import time
from tkinter import messagebox

height = 500
width = 500

left = 0
top = 3
bottom = height
right = width

# determines the size of the lift based on the number of
# lifts that can fit in the animation window.
length = 25
# coordinate system [left x1, top y1, right x2, bottom y2]


class root(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Lift Manager")
        self.canvas = tkinter.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0, relief='ridge', bg="lightblue")
        self.num_flrs = 10
        self.lift = self.canvas.create_rectangle(50, 4, 75, 28, fill="pink", outline='grey')
        self.shaft = self.canvas.create_rectangle(49, 3, 76, 400, fill="white", outline='black', width="1")
        self.canvas.tag_raise(self.shaft)
        self.canvas.tag_raise(self.lift)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.canvas.bind("<Configure>", self.redraw)
        self.status = tkinter.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")

    def redraw(self, event=None):
        self.canvas.delete("lift")
        self.canvas.winfo_height()
        self.canvas.winfo_height()

    def move(self):
        xspeed = 0
        yspeed = 1
        while True:
            self.canvas.move(self.lift, xspeed, yspeed)
            position = self.canvas.coords(self.lift)
            self.root.update()
            self.canvas.update()
            time.sleep(0.02)
            if position[3] >= bottom:
                yspeed = -yspeed
            elif position[1] == top:
                yspeed = -yspeed

def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        root.destroy()

if __name__ == "__main__":
    root = root()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.minsize(350, 300)
    root.mainloop()

