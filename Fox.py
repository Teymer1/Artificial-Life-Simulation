from Animal import Animal
import random

class Fox(Animal):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Fox";
     self.index = 0;
     self.power = 3;
     self.initiative = 7;
     self.color = "orange"


    def action(self, game_world, organism_vector):
      self.game_world = game_world
      self.WentUp = False
      self.WentDown = False
      self.WentLeft = False
      self.WentRight = False

      self.TriedUp = False
      self.TriedDown = False
      self.TriedLeft = False
      self.TriedRight = False
      self.organism_vector = organism_vector
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
            self.koord_y -= 1  # Move top
            for organism in self.organism_vector:
               if self.koord_x == organism.koord_x and self.koord_y == organism.koord_y and organism.power > self.power:
                   self.koord_y += 1
                   self.is_possible_go = False
                   break
            if self.is_possible_go:
             executed = True
             self.WentUp = True
        elif direction == 2 and self.koord_x != self.Width - 1:
           self.koord_x += 1  # Move right
           for organism in self.organism_vector:
               if self.koord_x == organism.koord_x and self.koord_y == organism.koord_y and organism.power > self.power:
                   self.koord_x -= 1
                   self.is_possible_go = False
                   break
           if self.is_possible_go:
             executed = True
             self.WentUp = True
        elif direction == 3 and self.koord_y != self.Height - 1:
            self.koord_y += 1  # Move down
            for organism in self.organism_vector:
               if self.koord_x == organism.koord_x and self.koord_y == organism.koord_y and organism.power > self.power:
                   self.koord_y -= 1
                   self.is_possible_go = False
                   break
            if self.is_possible_go:
             executed = True
             self.WentUp = True
        elif direction == 4 and self.koord_x != 0:
            self.koord_x -= 1  # Move left
            for organism in self.organism_vector:
               if self.koord_x == organism.koord_x and self.koord_y == organism.koord_y and organism.power > self.power:
                   self.koord_x += 1
                   self.is_possible_go = False
                   break
            if self.is_possible_go:
             executed = True
             self.WentUp = True
        direction = rand.randint(1, 4)
        
        if self.TriedUp and self.TriedDown and self.TriedLeft and self.TriedRight:
            executed = True

        #Collision
      for organism in self.organism_vector:
        self.is_moved_board = False
        if self.is_reproduction_collision(organism):
            break