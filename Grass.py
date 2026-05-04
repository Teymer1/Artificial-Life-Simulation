from Plants import Plants

class Grass(Plants):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Grass";
     self.index = 7;
     self.power = 0;
     self.initiative = 0;
     self.color = "green"