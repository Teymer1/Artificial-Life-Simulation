from Plants import Plants
import random

class Guarana(Plants):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Guarana";
     self.index = 9;
     self.power = 0;
     self.initiative = 0;
     self.color = "blue"

    def action(self, game_world, organism_vector):
     rand = random.Random()
     for i in range(3):
        is_spread = rand.randint(0, 1)
        if is_spread == 0:
            super().action(game_world, organism_vector)