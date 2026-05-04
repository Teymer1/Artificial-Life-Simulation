import random
import tkinter.messagebox as messagebox
import sys
from Organism import Organism
from Animal import Animal

class Turtle(Animal):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
        super().__init__(width, height, organism_vector, koord_x, koord_y)
        self.name = "Turtle"
        self.index = 6
        self.power = 2
        self.initiative = 1
        self.color = "hot pink"

    def action(self, game_world, organism_vector):
        self.organism_vector = organism_vector
        if random.random() < 0.25:
            super().action(game_world, self.organism_vector)

    def Collision(self, organism):
        if self.is_alzura_board(organism) or self.is_antelope_escape(organism):
            return

        if organism.power < 5 and organism.power < self.power:
            self._repel_attacker(organism)
            return

        if self.power >= organism.power:
            self._win_collision(organism)
        else:
            self._lose_collision(organism)

    def _repel_attacker(self, organism):
        step = 2 if getattr(organism, 'is_antelope', False) else 1
        
        if organism.WentDown: organism.koord_y -= step
        elif organism.WentUp: organism.koord_y += step
        elif organism.WentLeft: organism.koord_x += step
        elif organism.WentRight: organism.koord_x -= step

        Organism.results.append(
            f"{self.name} repelled {organism.name} back to ({organism.koord_x}, {organism.koord_y})"
        )

    def _win_collision(self, organism):
        Organism.results.append(
            f"{self.name}({self.power}) killed {organism.name}({organism.power}) at ({self.koord_x}, {self.koord_y})"
        )
        
        if organism.name == "Human":
            messagebox.showinfo("Game over", f"You were defeated by {self.name}!")
            sys.exit(0)

        if self.is_plus_3_power(organism):
            self.power += 3
            
        if organism in self.organism_vector:
            self.organism_vector.remove(organism)

    def _lose_collision(self, organism):
        self.is_lost = True
        Organism.results.append(
            f"{organism.name}({organism.power}) killed {self.name} at ({self.koord_x}, {self.koord_y})"
        )