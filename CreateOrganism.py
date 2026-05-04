import random
from typing import List

from Organism import Organism
from Fox import Fox
from Wolf import Wolf
from Sheep import Sheep
from Human import Human
from CyberSheep import CyberSheep
from Antelope import Antelope
from Turtle import Turtle
from Dandelion import Dandelion
from Grass import Grass
from Guarana import Guarana
from SosnowskyHogweed import SosnowskyHogweed
from Wolfberries import Wolfberries

class CreateOrganism:
    def __init__(self, width : int, height : int):
        self.organism_vector: List[Organism] = []
        max_quantity = 0
        if width * height <= 150 and width * height > 70:
            max_quantity = 2
        elif width * height <= 70:
            max_quantity = 1
        else:
            max_quantity = 3

        for creature_nr in range(12):
            if creature_nr <= 6:
                if creature_nr == 2:
                    self.organism_vector.append(Human(width=width, height=height, organism_vector=self.organism_vector))
                for ilosc_Animal in range(random.randint(2, max_quantity + 1)):
                    if creature_nr == 0:
                        self.organism_vector.append(Fox(width=width, height=height, organism_vector=self.organism_vector))
                    elif creature_nr == 1:
                        self.organism_vector.append(Wolf(width=width, height=height, organism_vector=self.organism_vector))
                    elif creature_nr == 3:
                        self.organism_vector.append(Sheep(width=width, height=height, organism_vector=self.organism_vector))
                    elif creature_nr == 4:
                        self.organism_vector.append(CyberSheep(width=width, height=height, organism_vector=self.organism_vector))
                    elif creature_nr == 5:
                        self.organism_vector.append(Antelope(width=width, height=height, organism_vector=self.organism_vector))
                    elif creature_nr == 6:
                        self.organism_vector.append(Turtle(width=width, height=height, organism_vector=self.organism_vector))
            elif creature_nr >= 7:
                for plant_quantity in range(random.randint(1, max_quantity)):
                    if creature_nr == 7:
                        self.organism_vector.append(Grass(width=width, height=height, organism_vector=self.organism_vector))
                    elif creature_nr == 8:
                        self.organism_vector.append(Dandelion(width=width, height=height, organism_vector=self.organism_vector))
                    elif creature_nr == 9:
                        self.organism_vector.append(Guarana(width=width, height=height, organism_vector=self.organism_vector))
                    elif creature_nr == 10:
                        self.organism_vector.append(Wolfberries(width=width, height=height, organism_vector=self.organism_vector))
                    elif creature_nr == 11:
                        self.organism_vector.append(SosnowskyHogweed(width=width, height=height, organism_vector=self.organism_vector))

    def getorganism_vector(self) -> List[Organism]:
        return self.organism_vector
