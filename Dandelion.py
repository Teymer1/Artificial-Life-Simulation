from Plants import Plants
import random

class Dandelion(Plants):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Dandelion";
     self.index = 8;
     self.power = 0;
     self.initiative = 0;
     self.color = "burlywood2"


    def action(self, game_world, organism_vector):
     rand = random.Random()
     for i in range(3):
            super().action(game_world, organism_vector)