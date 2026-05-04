from Animal import Animal

class Sheep(Animal):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Sheep";
     self.index = 3;
     self.power = 4;
     self.initiative = 4;
     self.color = "cyan"