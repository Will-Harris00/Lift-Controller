import tkinter as root
import random
class Window(root.Tk):
    def __init__(self, *args, **kwargs):
        self.floors = 10
        self.num_lifts = 1
        root.Tk.__init__(self, *args, **kwargs)
        self.title("Lift Manager")
        self.canvas = root.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = self.floors
        self.columns = self.num_lifts * 2
        self.lifts = {}
        self.canvas.bind("<Configure>", self.redraw)
        self.status = root.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")


    def redraw(self, event=None):
        self.canvas.delete("lfts")
        self.canvas.delete("flrs")
        cellwidth = int(self.canvas.winfo_width()/self.columns)
        cellheight = int(self.canvas.winfo_height()/self.rows)
        for column in range(self.columns):
            if column in range(1, (self.columns), 2):
                for row in range(self.rows):
                    x1 = column*cellwidth
                    y1 = row * cellheight
                    x2 = x1 + cellwidth
                    y2 = y1 + cellheight
                    lift_pos = self.canvas.create_rectangle(x1,y1,x2,y2, fill="lightblue", tags="lfts")
                    self.lifts[row, column] = lift_pos
                    print(lift_pos)
            elif column in range(0, (self.columns-1), 2):
                floor_num = 0
                for row in range(self.rows, 0, -1):
                    x1 = column * cellwidth
                    y1 = row * cellheight
                    x2 = x1 + (cellwidth//1.5)
                    y2 = y1 - (cellheight//1.5)
                    if floor_num == 0:
                        self.canvas.create_text(x2, y2, text="G", tags="flrs",
                                                font=('Arial', -round(cellheight//1.75)))
                    elif floor_num != 0:
                        self.canvas.create_text(x2, y2, text=str(floor_num), tags="flrs",
                                                font=('Arial', -round(cellheight // 1.75)))
                    floor_num += 1
        print("finished")
        self.travel()
        self.movement()

    def travel(self):
        self.dest = []
        start = random.randint(0, self.floors)
        end = random.randint(0, self.floors)
        self.dest.append(start)
        self.dest.append(end)
        return self.dest

    def movement(self):
        print(self.dest)
        if self.dest[0] == self.dest[1]:
            del self.dest[1], self.dest[0]
        elif self.dest[0] < self.dest[1]:
            for i in range(self.dest[0],self.dest[1]):
                print(i)
        else:
            for i in range(self.dest[1], self.dest[0], -1):
                print(i)
        print(self.lifts)
        lift_pos = self.floors + self.dest[0]
        print(self.lifts)
        print(lift_pos)
        lift_color = self.canvas.itemcget(lift_pos, "fill")
        new_color = "lightblue" if  lift_color == "lightpink" else "lightpink"
        self.canvas.itemconfigure(lift_pos, fill=new_color)





if __name__ == "__main__":
    window = Window()
    window.mainloop()