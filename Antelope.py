from Animal import Animal
from Organism import Organism
import random
import tkinter.messagebox as messagebox
import sys

class Antelope(Animal):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
        super().__init__(width, height, organism_vector, koord_x, koord_y)
        self.name = "Antelope"
        self.index = 5
        self.power = 4
        self.initiative = 4
        self.color = "saddle brown"
        self.is_antelope = True

    def action(self, game_world, organism_vector):
        self.game_world = game_world
        self.organism_vector = organism_vector

        old_x, old_y = self.koord_x, self.koord_y
        
        if not self._move_double():
             super().move_randomly() 

        for organism in list(self.organism_vector):
            if self is not organism and self.koord_x == organism.koord_x and self.koord_y == organism.koord_y:
                if self.is_reproduction_collision(organism):
                    break

    def _move_double(self):
        directions = [('Up', 0, -2), ('Down', 0, 2), ('Left', -2, 0), ('Right', 2, 0)]
        random.shuffle(directions)
        
        for name, dx, dy in directions:
            new_x = self.koord_x + dx
            new_y = self.koord_y + dy
            if 0 <= new_x < self.Width and 0 <= new_y < self.Height:
                for attr in ['WentUp', 'WentDown', 'WentLeft', 'WentRight']:
                    setattr(self, attr, False)
                self.koord_x, self.koord_y = new_x, new_y
                setattr(self, f'Went{name}', True)
                return True
        return False

    def antelope_escape(self, opponent):
        if random.randint(0, 1) == 0:
            Organism.results.append(f"{self.name} met {opponent.name}, but managed to escape!")
            self.move_randomly() 
        else:
            self.is_lost = True
            Organism.results.append(f"{self.name} met {opponent.name} and couldn't save herself.")

    def Collision(self, organism):
        if self.is_alzura_board(organism):
            return

        if self.power >= organism.power:
            if getattr(organism, 'index', -1) == 9: self.power += 3
            
            self.kill_organism(organism)
        else:
            self.antelope_escape(organism)