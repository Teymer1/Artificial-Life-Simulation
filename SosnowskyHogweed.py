from Plants import Plants
import random

class SosnowskyHogweed(Plants):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "SosnowskyHogweed";
     self.index = 11;
     self.power = 10;
     self.initiative = 0;
     self.color = "red"
     self.cybersheep_goal = True






