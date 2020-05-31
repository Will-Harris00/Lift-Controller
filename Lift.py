from tkinter import *
root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

column_size = str(screen_width//2)
print(column_size)
lift_1=Label(root, bg="lightblue")
lift_2=Label(root, bg="lightpink")

lift_1.grid(row=0, column=0)
lift_2.grid(row=0, column=1)
root.mainloop()
"""

left = 0
top = 3
bottom = height
right = width

# determines the size of the lift based on the number of
# lifts that can fit in the animation window.
length = 25
# coordinate system [left x1, top y1, right x2, bottom y2]

canvas = Canvas(root, height=height, width=width, bg="lightblue")
canvas.pack()

shaft = canvas.create_rectangle(49, top, 76, bottom, fill="white", outline='black', width="1")
lift = canvas.create_rectangle(50, top, 75, (top+length), fill="white", outline='grey')
xspeed = 0
yspeed = 1

while True:
    canvas.move(lift, xspeed, yspeed)
    position = canvas.coords(lift)

    root.update()
    time.sleep(0.02)
    if position[3]>=bottom:
        yspeed = -yspeed
    elif position[1]==top:
        yspeed = -yspeed
"""

