from ingredients.burger import Burger

class Zoo:

    """
    0: Turtle
    1: Elephant
    2: Giraffe
    3: Bird
    4: Rat
    5: Kangaroo
    """

    def __init__(self):
        self.unlocked = 0

        b = Burger()
        b.add_ingredient(0)
        self.recipe_book = [b]
    
    def upgrade(self):
        self.unlocked += 1
        
        b = Burger()
        b.add_ingredient(self.unlocked)
        self.recipe_book.append(b)
    
    def add_recipe(self, burger):
        self.recipe_book.append(burger)