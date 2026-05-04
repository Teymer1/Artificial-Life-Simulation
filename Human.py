from Animal import Animal
import tkinter.messagebox as messagebox
import sys

class Human(Animal):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
        super().__init__(width, height, organism_vector, koord_x, koord_y)
        self.name = "Human"
        self.index = 2
        self.power = 5
        self.initiative = 4
        self.color = "black"
        self.alzura_board = False
        self.skill_cooldown = 0

    def action(self, game_world, organism_vector):
        self.game_world = game_world
        self.organism_vector = organism_vector
        key = self.game_world.key

        old_x, old_y = self.koord_x, self.koord_y

        if key == 'Up' and self.koord_y > 0:
            self.koord_y -= 1
        elif key == 'Down' and self.koord_y < self.Height - 1:
            self.koord_y += 1
        elif key == 'Left' and self.koord_x > 0:
            self.koord_x -= 1
        elif key == 'Right' and self.koord_x < self.Width - 1:
            self.koord_x += 1

        is_even_row = (self.koord_y % 2 == 0)
        if key in ['Home', 'Prior', 'End', 'Next']:
            self._handle_hex_move(key, is_even_row)

        if old_x == self.koord_x and old_y == self.koord_y:
            return False

        for organism in list(self.organism_vector):
            if organism is not self and self.koord_x == organism.koord_x and self.koord_y == organism.koord_y:
                if self.is_reproduction_collision(organism):
                    break
        
        return True 

    def _handle_hex_move(self, key, is_even):
        if key == 'Home':  
            if self.koord_y > 0:
                if is_even and self.koord_x > 0: 
                    self.koord_x -= 1
                self.koord_y -= 1
        
        elif key == 'Prior':  
            if self.koord_y > 0:
                if not is_even and self.koord_x < self.Width - 1: 
                    self.koord_x += 1
                self.koord_y -= 1
        
        elif key == 'End':  
            if self.koord_y < self.Height - 1:
                if is_even and self.koord_x > 0: 
                    self.koord_x -= 1
                self.koord_y += 1
        
        elif key == 'Next':  
            if self.koord_y < self.Height - 1:
                if not is_even and self.koord_x < self.Width - 1: 
                    self.koord_x += 1
                self.koord_y += 1

    def breeding(self, partner):
        pass

    def Collision(self, organism):
        if self.is_alzura_board(organism):
            return

        super().Collision(organism)
        if self.is_lost:
            messagebox.showinfo("End of the game", f"You were killed by {organism.name}!")
            sys.exit(0)