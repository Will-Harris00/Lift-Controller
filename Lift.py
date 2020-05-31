from tkinter import *
import time

window = Tk()

height = 300
width = 300

canvas = Canvas(window, height=height, width=width, bg="lightblue")
window.title("Lift Animation")
canvas.pack()

sqr = canvas.create_rectangle(50, 50, 75, 75, fill="white", outline='grey')
xspeed = 0
yspeed = 1

while True:
    canvas.move(sqr, xspeed, yspeed)
    position = canvas.coords(sqr)

    window.update()
    time.sleep(0.02)
    if position[3]>=height:
        yspeed = -yspeed
    elif position[1]==1:
        yspeed = -yspeed


