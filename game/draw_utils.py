from os import listdir
from random import randint
from ingredients.base_animal import BaseAnimal

def rect_button(t, x, y, w, h, color, text, highlighted=False, font_size=50, text_color="black", highlight_color="#D5B60A"):     # x and y coords are center of button
    t.pu()     # Setup
    t.seth(0)
    t.color(color)
    t.pensize(1)

    t.goto(x-w/2, y+h/2)    # Box
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(w)
        t.rt(90)
        t.fd(h)
        t.rt(90)
    t.end_fill()
    t.pu()

    if highlighted:     # Highlight button if selected
        t.goto(x-w/2-10, y+h/2+10)
        t.pd()
        t.color(highlight_color)
        t.pensize(5)
        for i in range(2):
            t.fd(w+20)
            t.rt(90)
            t.fd(h+20)
            t.rt(90)
        t.pu()

    t.goto(x, y-font_size/2-10)    # Text
    t.color(text_color)
    t.write(text, False, align="center", font=("a", font_size))

def text(t, x, y, text, font_size=50, text_color="black"):      # x and y coords are center
    t.pu()    # Setup
    t.seth(0)
    t.color(text_color)
    t.pensize(1)

    t.goto(x, y-font_size/2-15)    # Text
    t.pd()
    t.write(text, False, align="center", font=("a", font_size))
    t.pu()

# def draw_animal(t, x, y, animal, size=100, color="black"):       # x and y coords are top left
#     t.pu()    # Setup
#     t.seth(0)
#     t.color(color)
#     t.pensize(1)

#     if animal == -1:
#         t.goto(x, y)    # Placeholder
#         t.pd()
#         t.begin_fill()
#         for i in range(4):
#             t.fd(size)
#             t.rt(90)
#         t.end_fill()
#         t.pu()

def draw_pen(t, x, y, o, animal, highlighted=False, highlight_color="#D5B60A", size=200):        # x and y coords are center
    t.pu()    # Setup
    t.seth(0)
    t.color("brown")
    t.pensize(20)

    t.goto(x-size/2, y+size/2)
    t.pd()
    for i in range(4):
        t.fd(size)
        t.rt(90)
    t.pu()


    t.goto(x, y)
    if o:
        draw_shape(t, x, y, animal)
    else:
        draw_shape(t, x, y, "lock")

    if highlighted:     # Highlight pen if selected
        t.pensize(5)
        t.goto(x-size/2-20, y+size/2+20)
        t.pd()
        t.color(highlight_color)
        t.pensize(5)
        for i in range(4):
            t.fd(size+40)
            t.rt(90)
        t.pu()

def party_select_pen(t, x, y, o, burger, highlighted=False, highlight_color="#D5B60A", size=200):        # x and y coords are center
    t.pu()    # Setup
    t.seth(0)
    t.color("brown")
    t.pensize(20)

    t.goto(x-size/2, y+size/2)
    t.pd()
    for i in range(4):
        t.fd(size)
        t.rt(90)
    t.pu()


    t.goto(x, y)
    if o and burger:
        draw_burger(t, x, y, burger)
    elif not o:
        draw_shape(t, x, y, "lock")

    if highlighted:     # Highlight pen if selected
        t.pensize(5)
        t.goto(x-size/2-20, y+size/2+20)
        t.pd()
        t.color(highlight_color)
        t.pensize(5)
        for i in range(4):
            t.fd(size+40)
            t.rt(90)
        t.pu()

def draw_burger_pen(t, x, y, burgers, highlighted=False, highlight_color="#D5B60A", w=200, h=750):        # x and y coords are center
    t.pu()    # Setup
    t.seth(0)
    t.color("brown")
    t.pensize(20)

    t.goto(x-w/2, y+h/2)
    t.pd()
    for i in range(2):
        t.fd(w)
        t.rt(90)
        t.fd(h)
        t.rt(90)
    t.pu()

    for burger in burgers:
        draw_burger(t, x, 125-h/2+randint(0, 500), burger)

    if highlighted:     # Highlight pen if selected
        t.goto(x-w/2-20, y+h/2+20)
        t.pd()
        t.color(highlight_color)
        t.pensize(5)
        for i in range(2):
            t.fd(w+40)
            t.rt(90)
            t.fd(h+40)
            t.rt(90)
        t.pu()

def draw_shape(t, x, y, shape, highlighted=False, highlight_color="#D5B60A"):     # shape parameter w/o path or file extension
    t.pu()
    t.seth(0)
    t.shape(f"images/{shape}.gif")

    if highlighted:     # Highlight button if selected
        t.goto(x-80, y+85)
        t.pd()
        t.color(highlight_color)
        t.pensize(5)
        for i in range(2):
            t.fd(170)
            t.rt(90)
            t.fd(170)
            t.rt(90)
        t.pu()

    t.goto(x, y)
    t.stamp()

def draw_burger(t, x, y, burger):
    for i, animal in enumerate(burger.stack):
        draw_shape(t, x, y+i*25, BaseAnimal.names[animal].lower())

def triangle_button(t, x, y, d, size, color, highlighted=False, highlight_color="#D5B60A"):     # x and y coords are middle of vertical side of button
    t.pu()     # Setup
    t.color(color)
    t.pensize(1)

    if d == "r":
        t.seth(-30)
    elif d == "l":
        t.seth(-90)
    t.goto(x, y+size/2)
    t.pd()
    t.begin_fill()
    for i in range(3):
        t.fd(size)
        t.rt(120)
    t.end_fill()
    t.pu()

    if highlighted:
        if d == "r":
            t.seth(-30)
            t.goto(x-9, y+size/2+17)
        elif d == "l":
            t.seth(-90)
            t.goto(x+9, y+size/2+17)
        t.color(highlight_color)
        t.pensize(5)
        t.pd()
        for i in range(3):
            t.fd(size+33)
            t.rt(120)
        t.pu()

def register_shapes(screen):
    for file in listdir("images"):
        screen.register_shape(f"images/{file}")