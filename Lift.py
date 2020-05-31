import tkinter as root
import time
from tkinter import messagebox
import random
class Window(root.Tk):
    def __init__(self, *args, **kwargs):
        self.lift_floor = 0
        self.motor_direction = 1
        self.iterations = 10
        self.num_floors = 10
        self.top_floor = self.num_floors - 1
        self.num_lifts = 1
        root.Tk.__init__(self, *args, **kwargs)
        self.title("Lift Manager")
        self.canvas = root.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = self.num_floors
        self.columns = self.num_lifts * 2
        self.lift_pos = {}
        self.canvas.bind("<Configure>", self.redraw)
        self.status = root.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")
        self.status.configure(text="Iterations: %s" % (self.iterations))
        self.running = False
        self.position = 0


    def redraw(self, event=None):
        self.canvas.delete("lfts")
        self.canvas.delete("flrs")
        cellwidth = int(self.canvas.winfo_width() / self.columns)
        cellheight = int(self.canvas.winfo_height() / self.rows)
        for column in range(self.columns):
            current_floor = self.top_floor
            if column in range(1, (self.columns), 2):
                for row in range(self.rows):
                    x1 = column*cellwidth
                    y1 = row * cellheight
                    x2 = x1 + cellwidth
                    y2 = y1 + cellheight
                    lift_pos = self.canvas.create_rectangle(x1,y1,x2,y2, fill="lightblue", tags="lfts")
                    self.lift_pos[self.num_lifts, current_floor] = lift_pos
                    current_floor -= 1
            elif column in range(0, (self.columns - 1), 2):
                floor_num = 0
                for row in range(self.rows, 0, -1):
                    x1 = column * cellwidth
                    y1 = row * cellheight
                    x2 = x1 + (cellwidth // 1.5)
                    y2 = y1 - (cellheight // 1.5)
                    if floor_num == 0:
                        self.canvas.create_text(x2, y2, text="G", tags="flrs",
                                                font=('Arial', -round(cellheight // 1.75)))
                    elif floor_num != 0:
                        self.canvas.create_text(x2, y2, text=str(floor_num), tags="flrs",
                                                font=('Arial', -round(cellheight // 1.75)))
                    floor_num += 1
        self.move()

    def run(self):
        while self.iterations > 0:
            self.iterations -= 1
            self.move()
            if self.position == self.top_floor or 0:
                self.motor_direction *= -1
            else:
                time.sleep(0.5)
                self.canvas.delete("lfts")
                self.position += self.motor_direction


    def move(self):
        self.lift = self.lift_pos[self.num_lifts, self.position]
        lift_color = self.canvas.itemcget(self.lift, "fill")
        new_color = "lightblue" if  lift_color == "lightpink" else "lightpink"
        self.canvas.itemconfigure(self.lift, fill=new_color)


    def passengers(self):
        self.waiting_dict = {}
        for i in range(0, self.iterations):
            self.begin_flr = random.randint(0, self.top_floor)
            self.choice = ['Up', 'Down']
            self.direction = random.choice(self.choice)
            self.waiting_dict.update({i: self.direction})
        print(self.waiting_dict)

def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        window.destroy()

if __name__ == "__main__":
    window = Window()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.minsize(350, 300)
    window.mainloop()