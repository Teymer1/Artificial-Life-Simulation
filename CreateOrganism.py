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
    def __init__(self, width: int, height: int):
        self.organism_vector: List[Organism] = []
        
        area = width * height
        if area <= 70:
            max_qty = 1
        elif area <= 150:
            max_qty = 2
        else:
            max_qty = 3

        animals = [Fox, Wolf, Sheep, CyberSheep, Antelope, Turtle]
        plants = [Grass, Dandelion, Guarana, Wolfberries, SosnowskyHogweed]

        self.organism_vector.append(Human(width=width, height=height, organism_vector=self.organism_vector))

        for animal_class in animals:
            quantity = random.randint(2, max_qty + 1)
            for _ in range(quantity):
                self.organism_vector.append(
                    animal_class(width=width, height=height, organism_vector=self.organism_vector)
                )

        for plant_class in plants:
            quantity = random.randint(1, max_qty)
            for _ in range(quantity):
                self.organism_vector.append(
                    plant_class(width=width, height=height, organism_vector=self.organism_vector)
                )

    def getorganism_vector(self) -> List[Organism]:
        return self.organism_vector