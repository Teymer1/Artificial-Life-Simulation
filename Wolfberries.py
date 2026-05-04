from Plants import Plants
import random

class Wolfberries(Plants):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Wolfberries";
     self.index = 10;
     self.power = 99;
     self.initiative = 0;
     self.color = "purple3"
