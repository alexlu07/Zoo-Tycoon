class Tile:
    def __init__(self):
        self.burger = None

    def on_enter(self, burger):
        pass

    def on_leave(self, burger):
        self.burger = None

    def activate(self):
        pass

    def deactivate(self):
        pass

    def toggle(self):
        pass


class Gate(Tile):
    def __init__(self, open=False):
        super().__init__()
        self.open = open
    
    def on_enter(self, burger):
        if self.open:
            self.burger = burger

        return self.open
    
    def activate(self):
        self.open = True
    
    def deactivate(self):
        self.open = False

    def toggle(self):
        self.open = not self.open


class Grass(Tile):
    def on_enter(self, burger):
        self.burger = burger

        return True


class Hole(Tile):
    def __init__(self, height):
        super().__init__()
        self.height = height

    def on_enter(self, burger):
        if burger.get_height() <= self.height:
            self.burger = burger

        return burger.get_height <= self.height


class Button(Tile):
    def __init__(self, height, device):
        super().__init__()
        self.height = height
        self.device = device

    def on_enter(self, burger):
        if burger.get_height >= self.height:
            self.device.toggle()

        return False


class Plate(Tile):
    def __init__(self, weight, device):
        super().__init__()
        self.weight = weight
        self.device = device

    def on_enter(self, burger):
        self.burger = burger

        if burger.get_weight() >= self.weight:
            self.device.activate()

        return True
    
    def on_leave(self):
        super().on_leave()

        self.device.deactivate()
    

class Poison(Tile):
    def on_enter(self, burger):
        self.burger = burger
        burger.kill()

        return True
    

class Smashable(Tile):
    def __init__(self, strength):
        super().__init__()
        self.strength = strength
        self.broken = False
    
    def on_enter(self, burger):
        if self.broken:
            self.burger = burger

        if burger.get_strength() >= self.strength:
            self.broken = True
        
        return self.broken


class Void(Tile):
    def on_enter(self, burger):
        if self.top_ability() == "fly":
            self.burger = burger
            return True
        
        return False


class Wall(Tile):
    def on_enter(self, burger):
        return False


class Water(Tile):
    def on_enter(self, burger):
        if burger.bot_ability() == "swim":
            self.burger = burger
            return True
        
        return False

class Door(Tile):
    def on_enter(self, burger):
        self.burger = burger

        return True