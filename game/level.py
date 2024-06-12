from tiles import *
from turtle import Turtle
from time import sleep
from draw_utils import *

class Level:
    def __init__(self, file):
        with open(file, "r") as f:
            self.upgrade = f.readline().split()[1]
            self.char_map = [f.readline().split() for i in range(8)]
        
        tile_map = {"g": Grass, "w": Water, "d": Door}

        self.map = [[None for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                self.map[i][j] = tile_map[self.char_map[i][j]]()

    def draw_level(self, t, screen, burgers):
        screen.tracer(0, 0)
        screen.bgcolor("black")
        t.hideturtle()
        t.speed(0)

        for i in range(8):
            for j in range(8):
                t.pu()
                t.seth(0)
                t.goto(-600+j*150, 600-i*150)
                if self.char_map[i][j] == "g":
                    t.color("green")
                elif self.char_map[i][j] == "w":
                    t.color("blue")
                elif self.char_map[i][j] == "d":
                    t.color("black")
                t.pd()
                t.begin_fill()
                for k in range(4):
                    t.fd(150)
                    t.rt(90)
                t.end_fill()
                screen.tracer(0, 0)
        
        for burger in burgers:
            draw_burger(t, -600+burger[2]*150+75, 600-burger[1]*150-75, burger[0])
        
        screen.update()

    def enter_tile(self, x, y, burger):
        if self.char_map[x][y] == "d":
            return 2
        if self.map[x][y].on_enter(burger):
            return 1
        return 0
