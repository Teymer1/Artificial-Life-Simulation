from Organism import Organism
import random
import tkinter.messagebox as messagebox
import sys

class Animal(Organism):
  is_moved_board = False

  def action(self, game_world, organism_vector):
    self.organism_vector = organism_vector
    self.game_world = game_world
    self.what_move(self)
    #  Collision
    for organism in self.organism_vector:
        self.is_moved_board = False
        if self.is_reproduction_collision(organism):
            break
    


  def what_move(self,organism):
    organism.WentUp = False
    organism.WentDown = False
    organism.WentLeft = False
    organism.WentRight = False
    organism.TriedUp = False
    organism.TriedDown = False
    organism.TriedLeft = False
    organism.TriedRight = False
    rand = random.Random()
    direction = rand.randint(1, 4)
    executed = False
    while not executed:
        if direction == 1:
            organism.TriedUp = True
        elif direction == 2:
            organism.TriedRight = True
        elif direction == 3:
            organism.TriedDown = True
        elif direction == 4:
            organism.TriedLeft = True

        if direction == 1 and organism.koord_y != 0:
            organism.koord_y -= 1  
            executed = True
            organism.WentUp = True
        elif direction == 2 and organism.koord_x != organism.Width - 1:
            organism.koord_x += 1  
            executed = True
            organism.WentRight = True
        elif direction == 3 and organism.koord_y != organism.Height - 1:
            organism.koord_y += 1 
            executed = True
            organism.WentDown = True
        elif direction == 4 and organism.koord_x != 0:
            organism.koord_x -= 1  
            executed = True
            organism.WentLeft = True
        direction = rand.randint(1, 4)   
        if organism.TriedUp and organism.TriedDown and organism.TriedLeft and organism.TriedRight:
            executed = True


  def is_reproduction_collision(self, organism):
    if self is not organism and self.name != organism.name and self.koord_x == organism.koord_x and self.koord_y == organism.koord_y:
        self.Collision(organism)
        return True
    elif self is not organism and self.name == organism.name and self.koord_x == organism.koord_x and self.koord_y == organism.koord_y:
         if self.reproduction_break == 0: 
              self.breeding(organism)
              return True
         else:
          self.moving_to_unoccupied_place(organism)
    return False

  def moving_to_unoccupied_place(self, organism):
      self.WentUp = False
      self.WentDown = False
      self.WentLeft = False
      self.WentRight = False

      self.TriedUp = False
      self.TriedDown = False
      self.TriedLeft = False
      self.TriedRight = False
      self.is_possible_go = True

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

        if direction == 1 and self.koord_y != 0:
            self.koord_y -= 1 
            if self.koord_x == organism.koord_x and self.koord_y == organism.koord_y and organism.index == self.index:
                   self.koord_y += 1
                   self.is_possible_go = False
                   break
            if self.is_possible_go:
             executed = True
             self.WentUp = True
        elif direction == 2 and self.koord_x != self.Width - 1:
           self.koord_x += 1  
           if self.koord_x == organism.koord_x and self.koord_y == organism.koord_y and organism.index == self.index:
                   self.koord_x -= 1
                   self.is_possible_go = False
                   break
           if self.is_possible_go:
             executed = True
             self.WentUp = True
        elif direction == 3 and self.koord_y != self.Height - 1:
            self.koord_y += 1 
            if self.koord_x == organism.koord_x and self.koord_y == organism.koord_y and organism.index == self.index:
                   self.koord_y -= 1
                   self.is_possible_go = False
                   break
            if self.is_possible_go:
             executed = True
             self.WentUp = True
        elif direction == 4 and self.koord_x != 0:
            self.koord_x -= 1 
            if self.koord_x == organism.koord_x and self.koord_y == organism.koord_y and organism.index == self.index:
                   self.koord_x += 1
                   self.is_possible_go = False
                   break
            if self.is_possible_go:
             executed = True
             self.WentUp = True
        direction = rand.randint(1, 4)
        
        if self.TriedUp and self.TriedDown and self.TriedLeft and self.TriedRight:
            executed = True
    

  def Collision(self, organism):
           if self.is_alzura_board(organism):
               pass
           elif self.power >= organism.power:
                if self.is_plus_3_power(organism):
                    self.power += 3
                if not organism.is_success_attack or (organism.is_success_attack and self.power >= 5):
                    if self.is_antelope_escape(organism):
                        pass
                    elif not self.is_antelope_escape(organism):
                        Organism.results.append(f"{self.name}(power:{self.power}) killed {organism.name}(power:{organism.power}) in ({organism.koord_x},{organism.koord_y})")
                        if organism.name == "Human":
                            messagebox.showinfo("Game over", "You lost \nTo close the game, press \"OK\"")
                            sys.exit(0)
                        self.organism_vector.remove(organism)
                elif organism.is_success_attack and self.power < 5:
                    if self.WentUp:
                        self.koord_y += 1
                    if self.WentDown:
                        self.koord_y -= 1
                    if self.WentLeft:
                        self.koord_x += 1
                    if self.WentRight:
                        self.koord_y -= 1
                    Organism.results.append(f"{self.name}(power:{self.power}) met {organism.name}(power:{organism.power}) in ({organism.koord_x},{organism.koord_y}) i wrocil sie na pozycje ({self.koord_x},{self.koord_y})")
           elif self.power < organism.power:
                self.is_lost = True
                Organism.results.append(f"{organism.name}(power:{organism.power}) killed {self.name}(power:{self.power}) in ({organism.koord_x},{organism.koord_y})")


  def breeding(self, organism):
                     from Fox import Fox
                     from Wolf import Wolf
                     from Sheep import Sheep
                     from CyberSheep import CyberSheep
                     from Antelope import Antelope
                     from Turtle import Turtle
                     if self.index == 0:
                            self.organism_vector.append(Fox(koord_x=self.koord_x, koord_y=self.koord_y, width=self.Width,height=self.Height))
                            Organism.results.append(f"After reproduction, an organism was created Fox in ({self.koord_x},{self.koord_y})")
                     elif self.index == 1:
                            self.organism_vector.append(Wolf(koord_x=self.koord_x, koord_y=self.koord_y, width=self.Width,height=self.Height))
                            Organism.results.append(f"After reproduction, an organism was created Wolf in ({self.koord_x},{self.koord_y})")
                     elif self.index == 3:
                            self.organism_vector.append(Sheep(koord_x=self.koord_x, koord_y=self.koord_y, width=self.Width,height=self.Height))
                            Organism.results.append(f"After reproduction, an organism was created Sheep in ({self.koord_x},{self.koord_y})")
                     elif self.index == 4:
                            self.organism_vector.append(CyberSheep(koord_x=self.koord_x, koord_y=self.koord_y, width=self.Width,height=self.Height))
                            Organism.results.append(f"After reproduction, an organism was created Cyber Sheep in ({self.koord_x},{self.koord_y})")
                     elif self.index == 5:
                            self.organism_vector.append(Antelope(koord_x=self.koord_x, koord_y=self.koord_y, width=self.Width,height=self.Height))
                            Organism.results.append(f"After reproduction, an organism was created Antelope in ({self.koord_x},{self.koord_y})")
                     elif self.index == 6:
                            self.organism_vector.append(Turtle(koord_x=self.koord_x, koord_y=self.koord_y, width=self.Width,height=self.Height))
                            Organism.results.append(f"After reproduction, an organism was created Turtle in ({self.koord_x},{self.koord_y})")
                     self.returning_to_position_after_breeding(self)
                     self.returning_to_position_after_breeding(organism)
                     self.reproduction_break = 30
                     organism.reproduction_break = 30


  def returning_to_position_after_breeding(self, organism):
      if organism.WentDown:
          organism.koord_y -= 1
      elif organism.WentLeft:
          organism.koord_x += 1
      elif organism.WentUp:
          organism.koord_y += 1
      elif organism.WentRight:
          organism.koord_y -= 1
   

  def is_free_space_after_breeding(self, koord_x_breeding : int, koord_y_breeding : int):
         is_free_space = 0
         for vector in self.organism_vector:
            if koord_x_breeding != vector.koord_x or koord_y_breeding != vector.koord_y:
                  is_free_space += 1
            if is_free_space == len(self.organism_vector):
                return True
         return False


  def is_antelope_escape(self, vektor):
    if vektor.is_antelope:
        czyzagine = random.randint(0, 1)
        if czyzagine == 1:
            return False
        elif czyzagine == 0:
            Organism.results.append(f"{self.name}(power:{self.power}) met {vektor.name}(power:{vektor.power}) in ({vektor.koord_x},{vektor.koord_y}), but")
            self.what_move(vektor)
            Organism.results.append(f"she managed to save herself ({vektor.koord_x},{vektor.koord_y})")
            return True
    else:
        return False

  def is_alzura_board(self, organism):
    if organism.alzura_board and organism.power <= self.power and self.is_moved_board == False:
        Organism.results.append(f"{self.name}(power:{self.power}) met {organism.name}(power:{organism.power}) in ({organism.koord_x},{organism.koord_y})")
        self.what_move(self)
        Organism.results.append(f"and through the Skill Alzura Board returned to position ({self.koord_x},{self.koord_y})")
        organism.is_moved_board = True
        return True
    elif self.alzura_board and self.power < organism.power and organism.index <= 6 and self.is_moved_board == False:
        Organism.results.append(f"{self.name}(power:{self.power}) met {organism.name}(power:{organism.power}) in ({self.koord_x},{self.koord_y})")
        self.what_move(organism)
        Organism.results.append(f"and through the Alzura Board Skill he moved it to the position ({organism.koord_x},{organism.koord_y})")
        organism.is_moved_board = True
        return True
    return False

  def is_plus_3_power(self, organism):
    if organism.index == 9:
        return True
    else:
        return False

    



