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
   def __init__(self, organism_vector, Index, cursor_x:int, cursor_y:int, Width:int, Height:int):
       self.organism_vector = organism_vector
       self.Index = Index

       if self.Index == 0:
            self.organism_vector.append(Fox(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Fox on ({cursor_x},{cursor_y})")
       elif self.Index == 1:
            self.organism_vector.append(Wolf(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Wolf on ({cursor_x},{cursor_y})")
       elif self.Index == 3:
            self.organism_vector.append(Sheep(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Sheep on ({cursor_x},{cursor_y})")
       elif self.Index == 4:
            self.organism_vector.append(CyberSheep(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Cyber Sheep on ({cursor_x},{cursor_y})")
       elif self.Index == 5:
            self.organism_vector.append(Antelope(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Antelope on ({cursor_x},{cursor_y})")
       elif self.Index == 6:
            self.organism_vector.append(Turtle(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Turtle on ({cursor_x},{cursor_y})")
       elif self.Index == 7:
            self.organism_vector.append(Grass(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Grass on ({cursor_x},{cursor_y})")
       elif self.Index == 8:
            self.organism_vector.append(Dandelion(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Dandelion on ({cursor_x},{cursor_y})")
       elif self.Index == 9:
            self.organism_vector.append(Guarana(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Guarana on ({cursor_x},{cursor_y})")
       elif self.Index == 10:
            self.organism_vector.append(Wolfberries(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - Wolfberries on ({cursor_x},{cursor_y})")
       elif self.Index == 11:
            self.organism_vector.append(SosnowskyHogweed(koord_x=cursor_x, koord_y=cursor_y, width=Width,height=Height))
            Organism.results.append(f"Created a new organism - SosnowskyHogweed on ({cursor_x},{cursor_y})")



