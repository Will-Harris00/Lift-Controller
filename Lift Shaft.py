import tkinter as tk
from tkinter import messagebox


class root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Lift Manager")
        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0, bg="lightblue")
        self.canvas.pack(fill="both", expand="true")
        self.numberOfFloors = 10
        self.canvas.bind("<Configure>", self.redraw)


    def redraw(self, event=None):
        self.canvas.delete("lift")
        self.canvas.delete("shaft")
        self.canvas.delete("flrnums")
        self.canvas.delete("statusbar")
        self.statusbar = tk.Label(self, anchor="sw")
        self.statusbar.configure(text="Number of floors: %s" % (self.numberOfFloors))
        self.frame = self.canvas.create_window(0, self.canvas.winfo_height(), window=self.statusbar, width=self.canvas.winfo_width(), height=self.statusbar.winfo_reqheight(), anchor="sw", tags="statusbar")
        self.lift = self.canvas.create_rectangle(self.canvas.winfo_width() / 2, 1,
                                                 self.canvas.winfo_width() - 3,
                                                 (self.canvas.winfo_height() / self.numberOfFloors) - 1,
                                                 fill="pink", outline='grey', tags="lift")
        self.shaft = self.canvas.create_rectangle((self.canvas.winfo_width() / 2) - 1, 0,
                                                  self.canvas.winfo_width() - 2,
                                                  self.canvas.winfo_height() - (self.statusbar.winfo_reqheight() + 2), fill="white",
                                                  outline='black', width="1", tags="shaft")
        tk.Tk.update(self)
        for i in range(self.numberOfFloors):
            # change the i at the end of the line to multiple -12 by either one or zero depending on if the floor number is zero or not
            j = i
            j = int(j > 0)
            self.floor_numbers = self.canvas.create_text(10, -12 + (self.canvas.winfo_height() - self.statusbar.winfo_reqheight()) - (((i) * (self.canvas.winfo_height()/(self.numberOfFloors))) - (12 * j)), text=str(i), tags="flrnums", font=('Arial', 12))
        self.canvas.tag_raise(self.shaft)
        self.canvas.tag_raise(self.lift)


def on_closing():
    if messagebox.askokcancel("Exit program", "Do you want to quit?"):
        root.destroy()


if __name__ == "__main__":
    root = root()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.minsize(350, 300)
    #root.pack_propagate(1)
    #root.update_idletasks()
    root.mainloop()

