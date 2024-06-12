from ingredients.base_animal import BaseAnimal

class Burger:
    def __init__(self):
        self.stack = []
        self.passenger = None
    
    def add_ingredient(self, ingredient):
        if not self.stack or self.get_weight() < self.get_strength():
            self.stack.append(ingredient)
            return True

        return False
    
    def get_strength(self):
        return BaseAnimal.strength[self.stack[0]]
    
    def get_weight(self):
        return sum([BaseAnimal.weight[i] for i in self.stack])
    
    def get_height(self):
        return sum([BaseAnimal.height[i] for i in self.stack])
    
    def top_ability(self):
        return BaseAnimal.top_ability[self.stack[-1]]
    
    def bot_ability(self):
        return BaseAnimal.bot_ability[self.stack[0]]

    def kill(self):
        self.stack.pop(0)

    def dead(self):
        if not self.stack:
            return True
        
        return False