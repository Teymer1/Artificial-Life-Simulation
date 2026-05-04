from Animal import Animal

class Wolf(Animal):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Wolf";
     self.index = 1;
     self.power = 9;
     self.initiative = 5;
     self.color = "grey"