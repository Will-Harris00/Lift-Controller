import tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        floors = int(input("Number of floors "))
        lifts = int(input("Number of lifts "))
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = floors
        self.columns = lifts * 2
        self.tiles = {}
        self.canvas.bind("<Configure>", self.redraw)
        self.status = tk.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")

    def redraw(self, event=None):
        self.canvas.delete("rect")
        cellwidth = int(self.canvas.winfo_width()/self.columns)
        cellheight = int(self.canvas.winfo_height()/self.rows)
        for column in range(0, (self.columns-1), 2):
            for row in range(self.rows):
                x1 = column*cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                tile = self.canvas.create_rectangle(x1,y1,x2,y2, fill="lightblue", tags="rect")
                self.tiles[row, column] = tile
#                self.canvas.tag_bind(tile, "<1>", lambda event, row=row, column=column: self.clicked(row, column))
        for column in range(1, (self.columns), 2):
            floor_num = 0
            for row in range(self.rows):
                floor_num += 1
                tk.Label(self.canvas, text=str(floor_num), fg='white', bg='lightpink').grid(row=row)

    def clicked(self, row, column):
        tile = self.tiles[row, column]
        tile_color = self.canvas.itemcget(tile, "fill")
        new_color = "lightblue" if  tile_color == "lightpink" else "lightpink"
        self.canvas.itemconfigure(tile, fill=new_color)
        self.status.configure(text="you clicked on %s/%s" % (row, column))

if __name__ == "__main__":
    app = App()
    app.mainloop()