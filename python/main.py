import turtle
import numpy as np

WIDTH, HEIGHT = 1000, 1000

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Turtle")

contours = np.load("assets/turtle/outlines/elephant.npz")
contours = [contours[i] for i in contours.files]

ele_t = turtle.Turtle()

ele_t.speed(0)

def transform(x, y, abc=0):
#    return int((x-872)/3)+abc, -int((y-1200)/3)
    return int((x-872)/10)+abc, -int((y-1200)/10)

screen.tracer(0)

import time
time.sleep(3)

for abc in range(1000):
    ele_t.clear()
    for c in contours:

        ele_t.penup()
        ele_t.goto(transform(*c[0][0], abc=abc))
        ele_t.pendown()
        for i in c:
            i = i[0]
            ele_t.goto(transform(i[0], i[1], abc=abc))
        ele_t.goto(transform(*c[0][0], abc=abc))

    screen.update()

time.sleep(3)

screen.mainloop()
