from Organism import Organism
from Fox import Fox
from Wolf import Wolf
from Sheep import Sheep
from CyberSheep import CyberSheep
from Antelope import Antelope
from Turtle import Turtle
from Dandelion import Dandelion
from Grass import Grass
from Guarana import Guarana
from SosnowskyHogweed import SosnowskyHogweed
from Wolfberries import Wolfberries

class AddingOrganism:
    def __init__(self, organism_vector, index, cursor_x, cursor_y, width, height):
        creature_map = {
            0: Fox, 1: Wolf, 3: Sheep, 4: CyberSheep,
            5: Antelope, 6: Turtle, 7: Grass, 8: Dandelion,
            9: Guarana, 10: Wolfberries, 11: SosnowskyHogweed
        }

        creature_class = creature_map.get(index)

        if creature_class:
            new_organism = creature_class(
                koord_x=cursor_x, 
                koord_y=cursor_y, 
                width=width, 
                height=height
            )
            organism_vector.append(new_organism)
            
            msg = f"Created a new organism - {new_organism.name} on ({cursor_x},{cursor_y})"
            Organism.results.append(msg)
