from Animal import Animal
from Organism import Organism
import random
import tkinter.messagebox as messagebox
import sys

class Antelope(Animal):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Antelope";
     self.index = 5;
     self.power = 4;
     self.initiative = 4;
     self.color = "saddle brown"
     self.is_antelope = True


    def action(self, game_world, organism_vector):
      self.WentUp = False
      self.WentDown = False 
      self.WentLeft = False
      self.WentRight = False

      self.TriedUp = False
      self.TriedDown = False
      self.TriedLeft = False
      self.TriedRight = False

      self.game_world = game_world
      self.organism_vector = organism_vector
      rand = random.Random()
      direction = rand.randint(1, 4)

      executed = False
      while not executed:
        if direction == 1:
          self.TriedUp = True
        elif direction == 2:
          self.TriedRight = True
        elif direction == 3:
          self.TriedDown = True
        elif direction == 4:
          self.TriedLeft = True

        if direction == 1 and self.koord_y > 1:
           self.koord_y -= 2  
           executed = True
           self.WentUp = True
        elif direction == 2 and self.koord_x < self.Width-2:
           self.koord_x += 2  
           executed = True
           self.WentRight = True
        elif direction == 3 and self.koord_y < self.Height-2:
           self.koord_y += 2  
           executed = True
           self.WentDown = True
        elif direction == 4 and self.koord_x > 1:
          self.koord_x -= 2  
          executed = True
          self.WentLeft = True
        direction = rand.randint(1, 4)

        if self.TriedUp and self.TriedDown and self.TriedLeft and self.TriedRight:
          executed = True

      for organism in self.organism_vector:
         self.is_moved_board = False
         if self.is_reproduction_collision(organism):
           break

    def Collision(self, organism):
            if self.is_alzura_board(organism):
                pass
            elif self.power >= organism.power:
                if self.is_plus_3_power(organism):
                    self.power += 3
                if not organism.is_success_attack:
                    if organism.name == "Human":
                            messagebox.showinfo("Game over", "You lost\nTo close the game, press \"OK\"")
                            sys.exit(0)
                    Organism.results.append(f"{self.name}(power:{self.power}) killed {organism.name}(power:{organism.power}) in ({self.koord_x},{self.koord_y})")
                    self.organism_vector.remove(organism)
                elif organism.is_success_attack:
                    Organism.results.append(f"{self.name}(power:{self.power}) met {organism.name}(power:{organism.power}) in ({organism.koord_x},{organism.koord_y})")
                    if self.WentUp:
                        self.koord_y += 2
                    if self.WentDown:
                        self.koord_y -= 2
                    if self.WentLeft:
                        self.koord_x += 2
                    if self.WentRight:
                        self.koord_y -= 2
                    Organism.results.append(f"and returned to position ({self.koord_x},{self.koord_y})")
            elif self.power < organism.power:
                self.antelope_escape(organism)


    def antelope_escape(self, vektor):
     is_Smierc = random.randint(0, 1)
     if is_Smierc == 1:
        self.is_lost = True
        Organism.results.append(f"{self.name}(power:{self.power}) met {vektor.name}(power:{vektor.power}) in ({vektor.koord_x},{vektor.koord_y})")
        Organism.results.append("and couldn't save herself")
     elif is_Smierc == 0:
        Organism.results.append(f"{self.name}(power:{self.power}) met {vektor.name}(power:{vektor.power}) in ({vektor.koord_x},{vektor.koord_y})")
        self.what_move(self)
        Organism.results.append(f"and managed to save herself ({self.koord_x},{self.koord_y})")




