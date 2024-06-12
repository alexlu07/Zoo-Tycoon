from turtle import Turtle, Screen
from time import sleep
import keyboard
from draw_utils import *
from ingredients.burger import Burger
from tiles import *
from zoo import Zoo
from ingredients.base_animal import BaseAnimal
from level import Level


class Game:

    game_object = None

    def __init__(self):
        Game.game_object = self
        self.view = 0
        self.zoo = Zoo()

        self.levels = self.load_levels()
        self.level = 1              # Latest unlocked level
        self.selected_level = 1     # Currently selected level
        self.party = [None, None, None, None]
        self.party_slots = 1

        self.screen = Screen()
        self.screen.setup(1250, 1250)
        self.screen.listen()
        self.screen.title("Burger Zoo")
        self.screen.tracer(0)
        register_shapes(self.screen)

        # self.screen.manual_update = self.screen.update
        # self.screen.update = lambda: None;

        self.kb_input = {"up": False, "down": False, "left": False, "right": False, "space": False}
        keyboard.add_hotkey("up", self.up)
        keyboard.add_hotkey("down", self.down)
        keyboard.add_hotkey("left", self.left)
        keyboard.add_hotkey("right", self.right)
        keyboard.add_hotkey("space", self.space)

    def update(self):
        self.screen.clearscreen()

        if self.view == 0:        # Start screen
            self.start_screen()
        
        elif self.view == 1:      # Zoo
            self.zoo_screen()

        elif self.view == 2:      # Recipe Book
            self.recipe_book()

        elif self.view == 3:      # Kitchen
            self.kitchen()

        elif self.view == 4:       # Tutorial/Explanation
            self.tutorial_screen()

        elif self.view == 5:      # Level Select
            self.level_select()

        elif self.view == 6:      # Party Select
            self.party_select()

        elif self.view == 7:      # Level
            self.play_level()

    def start_screen(self):
        self.screen.tracer(0, 0)
        t = Turtle()
        t.hideturtle()
        t.speed(0)
        self.screen.bgcolor("#F3FFB6")

        rect_button(t, 0, -200, 300, 100, "#D38B5D", "Start", highlighted=True, font_size=50, text_color="black")
        text(t, 0, 200, "Burger Zoo", 125)

        self.screen.update()
        
        while True:
            if self.kb_input["space"]:
                self.kb_input["space"] = False
                self.view = 4
                break

            sleep(0.05)

    def tutorial_screen(self):
        self.screen.tracer(0, 0)
        t = Turtle()
        t.hideturtle()
        t.speed(0)
        self.screen.bgcolor("#F3FFB6")

        tutorial ="""
Lorem ipsum dolor sit amet.
Est voluptatem distinctio
est fuga odit qui esse illo
At internos quas in voluptas
nemo non sapiente nisi aut
nihil consequatur. Hic nemo
repellendus sit odio sapiente
cum laudantium ipsam est nihil
quaerat vel maxime tempore et
voluptates blanditiis est
impedit sint?
"""

        rect_button(t, 0, -500, 300, 100, "#D38B5D", "Continue", highlighted=True, font_size=50, text_color="black")
        text(t, 0, 400, "How to Play", 125)
        text(t, 0, -400, tutorial)

        self.screen.update()

        while True:
            if self.kb_input["space"]:
                self.kb_input["space"] = False
                self.view = 1
                break

            sleep(0.05)

    """
    [ ] [ ] [ ]  [recipes ] 
    [ ] [ ] | |  [kitchen ]
    [ ] [ ] [ ]  [wild    ]
    """
    def zoo_screen(self):
        selected = [0, 0]
        update = True
        animal = -1
        action = False

        self.screen.tracer(0, 0)
        t = Turtle()
        t.hideturtle()
        t.speed(0)

        while True:
            if self.kb_input["up"] and selected[0] > 0 and selected[1] != 2:
                selected[0] -= 1
                update = True

            elif self.kb_input["down"] and selected[0] < 2 and selected[1] != 2:
                selected[0] += 1
                update = True
                
            elif self.kb_input["right"] and selected[1] < 3:
                selected[1] += 1
                update = True

            elif self.kb_input["left"] and selected[1] > 0:
                selected[1] -= 1
                update = True

            elif self.kb_input["space"]:
                action = True
                if selected[1] >= 2:
                    update = True

            self.kb_input = {"up": False, "down": False, "left": False, "right": False, "space": False}

            if update:
                self.screen.clear()
                self.screen.bgcolor("#558B6E")

                # Top bar
                self.screen.tracer(0, 0)
                rect_button(t, 0, 575, 1250, 100, "#F3FFB6", "Burger Zoo")

                # Animal pens
                for i in range(6):
                    highlighted = False
                    if selected[0] == i//2 and selected[1] == i%2:
                        highlighted = True
                        animal = i

                    open = self.zoo.unlocked >= i

                    draw_pen(t, -450+275*(i%2), 350-275*(i//2), open, BaseAnimal.names[i].lower(), highlighted)     # .lower() cuz image files are lowercase, bc reasons

                # Burger pen
                draw_burger_pen(t, 100, 75, self.zoo.recipe_book, selected[1] == 2)

                # Tutorial, Kitchen, Level Select
                draw_shape(t, 400, 350, "book", selected[0] == 0 and selected[1] == 3)
                draw_shape(t, 400, 75, "utensils", selected[0] == 1 and selected[1] == 3)
                draw_shape(t, 400, -200, "door", selected[0] == 2 and selected[1] == 3)

                # Bottom bar
                rect_button(t, 0, -500, 1250, 250, "#F3FFB6", "")
                if selected[1] <= 1:    # Animal pen bottom bar
                    name = BaseAnimal.names[animal]
                    stats = [BaseAnimal.strength[animal], BaseAnimal.weight[animal], BaseAnimal.height[animal]]
                    if self.zoo.unlocked < animal:      # Hide unlocked animal info
                        name = "?" * len(name)
                        stats = ["?", "?", "?"]

                    rect_button(t, 0, -450, 500, 75, "#D38B5D", name, True)
                    text(t, 0, -550, f"Strength: {stats[0]}\tWeight: {stats[1]}\tHeight: {stats[2]}", 40)
                else:
                    if selected[1] == 2:    # Burger pen/Kitchen select
                        rect_button(t, 0, -500, 500, 75, "#D38B5D", "Recipe Book", True)
                        if action:
                            self.view = 2
                            break
                    
                    elif selected[0] == 0:
                        rect_button(t, 0, -500, 500, 75, "#D38B5D", "Tutorial", True)
                        if action:
                            self.view = 4
                            break

                    elif selected[0] == 1:
                        rect_button(t, 0, -500, 500, 75, "#D38B5D", "Kitchen", True)
                        if action:
                            self.view = 3
                            break
                    
                    elif selected[0] == 2:
                        rect_button(t, 0, -500, 500, 75, "#D38B5D", "Level Select", True)
                        if action:
                            self.view = 5
                            break


                self.screen.update()
                self.screen.tracer(0, 0)
                action = False
                update = False

            sleep(.05)

    def recipe_book(self):
        update = True
        action = False
        burger = 0

        self.screen.tracer(0, 0)
        t = Turtle()
        t.hideturtle()
        t.speed(0)

        while True:
            if self.kb_input["right"]:
                burger = (burger+1)%len(self.zoo.recipe_book)
                update = True

            elif self.kb_input["left"]:
                burger = (burger-1)%len(self.zoo.recipe_book)
                update = True

            elif self.kb_input["space"]:
                self.view = 1
                break

            self.kb_input = {"up": False, "down": False, "left": False, "right": False, "space": False}

            if update:
                self.screen.clear()
                self.screen.bgcolor("#558B6E")

                # Title
                self.screen.tracer(0, 0)
                rect_button(t, 0, 575, 1250, 100, "#F3FFB6", "Recipe Book", font_size=50)

                # Burger menu
                rect_button(t, 0, 50, 420, 720, "black", "")
                rect_button(t, 0, 50, 400, 700, "#F2F3F4", "")
                draw_shape(t, 0, -250, "plate")
                draw_burger(t, 0, -200, self.zoo.recipe_book[burger])

                # Arrow buttons
                triangle_button(t, 250, 50, "r", 100, "#D38B5D", True)
                triangle_button(t, -250, 50, "l", 100, "#D38B5D", True)

                # Back button
                rect_button(t, 0, -500, 1250, 230, "#F3FFB6", "")
                rect_button(t, 0, -500, 500, 100, "#D38B5D", "Back", True)
                
                self.screen.update()
                self.screen.tracer(0, 0)
                update = False

            sleep(.05)

    def kitchen(self):
        selected = [0, 0]
        update = True
        action = False
        burger = Burger()

        self.screen.tracer(0, 0)
        t = Turtle()
        t.hideturtle()
        t.speed(0)

        while True:
            if self.kb_input["up"] and selected[0] > 0:
                selected[0] -= 1
                update = True

            elif self.kb_input["down"] and selected[0] < 3:
                selected[0] += 1
                update = True
                
            elif self.kb_input["right"] and selected[1] < 1:
                selected[1] += 1
                update = True

            elif self.kb_input["left"] and selected[1] > 0:
                selected[1] -= 1
                update = True

            elif self.kb_input["space"]:
                action = True
                update = True

            self.kb_input = {"up": False, "down": False, "left": False, "right": False, "space": False}

            if update:
                self.screen.clear()
                self.screen.bgcolor("#558B6E")

                # Top bar
                self.screen.tracer(0, 0)
                rect_button(t, 0, 575, 1250, 100, "#F3FFB6", "Kitchen")

                # Animals
                for i in range(6):
                    highlighted = False
                    if selected[0] == i//2 and selected[1] == i%2:
                        highlighted = True
                        animal = i
                        if action and self.zoo.unlocked >= i:
                            burger.add_ingredient(i)

                    open = self.zoo.unlocked >= i

                    draw_pen(t, -450+275*(i%2), 350-275*(i//2), open, BaseAnimal.names[i].lower(), highlighted)     # .lower() cuz image files are lowercase, bc reasons

                # Burger view
                rect_button(t, 275, 50, 420, 720, "black", "")
                rect_button(t, 275, 50, 400, 700, "#F2F3F4", "")
                draw_shape(t, 275, -250, "plate")
                draw_burger(t, 275, -200, burger)

                # Bottom bar
                rect_button(t, 0, -500, 1250, 250, "#F3FFB6", "")
                rect_button(t, -300, -500, 500, 100, "#D38B5D", "Delete", selected[0] == 3 and selected[1] == 0)
                rect_button(t, 300, -500, 500, 100, "#D38B5D", "Create", selected[0] == 3 and selected[1] == 1)
                if action:
                    if selected[0] == 3 and selected[1] == 0 and not burger.dead():
                        burger.stack.pop(-1)
                        update = True
                        action = False
                        continue
                    
                    elif selected[0] == 3 and selected[1] == 1:
                        if not burger.dead():
                            self.zoo.add_recipe(burger)

                        self.view = 1
                        break


                self.screen.update()
                self.screen.tracer(0, 0)
                action = False
                update = False

            sleep(.05)
    
    def level_select(self):
        update = True
        action = False
        selected = [0, 0]
        level = 0

        self.screen.tracer(0, 0)
        t = Turtle()
        t.hideturtle()
        t.speed(0)

        while True:
            if self.kb_input["up"] and selected[0] > 0:
                selected[0] -= 1
                update = True

            elif self.kb_input["down"] and selected[0] < 3:
                selected[0] += 1
                update = True
                
            elif self.kb_input["right"] and selected[1] < 3:
                selected[1] += 1
                update = True

            elif self.kb_input["left"] and selected[1] > 0:
                selected[1] -= 1
                update = True

            elif self.kb_input["space"]:
                action = True
                update = True

            self.kb_input = {"up": False, "down": False, "left": False, "right": False, "space": False}

            if update:
                self.screen.clear()
                self.screen.bgcolor("#558B6E")

                # Title
                self.screen.tracer(0, 0)
                rect_button(t, 0, 575, 1250, 100, "#F3FFB6", "Level Select", font_size=50)

                # Levels
                for i in range(16):
                    highlighted = False
                    if selected[0]*4 + selected[1] == i:
                        highlighted = True

                    if i <= self.level-1:
                        rect_button(t, -450+293*(i%4), 350-250*(i//4), 250, 200, "#D38B5D", i+1, highlighted, font_size=75)
                    else:
                        rect_button(t, -450+293*(i%4), 350-250*(i//4), 250, 200, "#F3FFB6", "", highlighted, font_size=75)
                        draw_shape(t, -450+293*(i%4), 350-250*(i//4), "lock")

                if action and selected[0]*4 + selected[1] <= self.level-1:
                    self.view = 6
                    self.selected_level = selected[0]*4 + selected[1] + 1
                    break

                self.screen.update()
                self.screen.tracer(0, 0)
                update = False
                action = False

            sleep(.05)

    def party_select(self):
        selected = [0, 0, 0]
        update = True
        action = False
        burger = 0
        self.party = [None, None, None, None]

        self.screen.tracer(0, 0)
        t = Turtle()
        t.hideturtle()
        t.speed(0)

        while True:
            if selected[2] == 0:
                if self.kb_input["up"] and selected[0] > 0:
                    selected[0] -= 1
                    update = True

                elif self.kb_input["down"] and selected[0] < 2:
                    selected[0] += 1
                    update = True
                    
                elif self.kb_input["right"] and selected[1] < 1:
                    selected[1] += 1
                    update = True

                elif self.kb_input["left"] and selected[1] > 0:
                    selected[1] -= 1
                    update = True

                elif self.kb_input["space"]:
                    action = True
                    update = True

            elif selected[2] == 1:
                if self.kb_input["right"]:
                    burger = (burger+1)%len(self.zoo.recipe_book)
                    self.party[selected[0]*2+selected[1]] = self.zoo.recipe_book[burger]
                    update = True

                elif self.kb_input["left"]:
                    burger = (burger-1)%len(self.zoo.recipe_book)
                    self.party[selected[0]*2+selected[1]] = self.zoo.recipe_book[burger]
                    update = True

                elif self.kb_input["space"]:
                    selected[2] = 0
                    update = True

            self.kb_input = {"up": False, "down": False, "left": False, "right": False, "space": False}

            if update:
                self.screen.clear()
                self.screen.bgcolor("#558B6E")

                # Top bar
                self.screen.tracer(0, 0)
                rect_button(t, 0, 575, 1250, 100, "#F3FFB6", "Party Select")

                # Animals
                for i in range(4):
                    highlighted = False
                    if selected[0] == i//2 and selected[1] == i%2 and selected[2] == 0:
                        highlighted = True
                        if self.party_slots >= i+1 and action:
                            self.party[i] = self.zoo.recipe_book[burger]
                            selected[2] = 1
                            highlighted = False

                    open = self.party_slots >= i+1

                    party_select_pen(t, -475+275*(i%2), 200-275*(i//2), open, self.party[i], highlighted)

                # Burger view
                rect_button(t, 275, 50, 370, 720, "black", "")
                rect_button(t, 275, 50, 350, 700, "#F2F3F4", "")
                draw_shape(t, 275, -250, "plate")
                if selected[2] == 1:
                    draw_burger(t, 275, -200, self.party[selected[0]*2+selected[1]])

                # Arrow buttons
                triangle_button(t, 500, 50, "r", 100, "#D38B5D", selected[2] == 1)
                triangle_button(t, 50, 50, "l", 100, "#D38B5D", selected[2] == 1)

                # Bottom bar
                rect_button(t, 0, -500, 1250, 250, "#F3FFB6", "")
                rect_button(t, -450, -500, 300, 100, "#D38B5D", "Back", selected[0] == 2 and selected[1] == 0)
                rect_button(t, -100, -500, 300, 100, "#D38B5D", "Start", selected[0] == 2 and selected[1] == 1)
                rect_button(t, 305, -500, 300, 100, "#D38B5D", "Select", selected[2] == 1)
                if action and selected[2] == 0:
                    if selected[0] == 2 and selected[1] == 0:
                        self.view = 1
                        break
                    elif selected[0] == 2 and selected[1] == 1:
                        a = True
                        for i, b in enumerate(self.party):
                            if not b and i+1 <= self.party_slots:
                                a = False
                        if a:
                            self.view = 7
                            break

                self.screen.update()
                self.screen.tracer(0, 0)
                action = False
                update = False

            sleep(.05)

    def play_level(self):
        t = Turtle()
        update = True
        level = self.levels[self.level-1]
        b = 0
        burgers = []
        for i in range(self.party_slots):
            burgers.append([self.party[i], 7, i])
        
        while True:
            if self.kb_input["up"]:
                if level.enter_tile(burgers[b][1]-1, burgers[b][2], burgers[b][0]):
                    burgers[b][1] -= 1
                update = True

            elif self.kb_input["down"]:
                if level.enter_tile(burgers[b][1]+1, burgers[b][2], burgers[b][0]):
                    burgers[b][1] += 1
                update = True
                
            elif self.kb_input["right"]:
                if level.enter_tile(burgers[b][1], burgers[b][2]+1, burgers[b][0]):
                    burgers[b][2] += 1
                update = True

            elif self.kb_input["left"]:
                if level.enter_tile(burgers[b][1], burgers[b][2]-1, burgers[b][0]):
                    burgers[b][2] -= 1
                update = True

            elif self.kb_input["space"]:
                b = (b+1)%self.party_slots
                update = True

            self.kb_input = {"up": False, "down": False, "left": False, "right": False, "space": False}

            if update:
                self.screen.clear()
                level.draw_level(t, self.screen, burgers)

                if level.char_map[burgers[b][1]][burgers[b][2]] == "d":
                    self.zoo.upgrade()
                    self.party_slots += 1
                    self.view = 1
                    break
                update = False

            sleep(.05)

    def load_levels(self):
        return [Level("levels/1.txt")]
    
    def reset(self):
        self.kb_input = {"up": False, "down": False, "left": False, "right": False, "space": False}
        self.screen.clearscreen()

    @staticmethod
    def up():
        Game.game_object.kb_input["up"] = True

    @staticmethod
    def down():
        Game.game_object.kb_input["down"] = True
    
    @staticmethod
    def left():
        Game.game_object.kb_input["left"] = True
    
    @staticmethod
    def right():
        Game.game_object.kb_input["right"] = True
    
    @staticmethod
    def space():
        Game.game_object.kb_input["space"] = True