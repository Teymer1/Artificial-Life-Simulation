from Animal import Animal
import tkinter.messagebox as messagebox
import sys

class Human(Animal):
   def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Human";
     self.index = 2;
     self.power = 5;
     self.initiative = 4;
     self.color = "black"
     self.alzura_board = False
     self.skill_cooldown = 0

   def action(self, game_world, organism_vector):
    self.game_world = game_world
    self.organism_vector = organism_vector

    if self.game_world.key == 'Up' and self.koord_y != 0:
        self.koord_y -= 1
    elif self.game_world.key == 'Down' and self.koord_y != self.Height - 1:
        self.koord_y += 1
    elif self.game_world.key == 'Left' and self.koord_x != 0:
        self.koord_x -= 1
    elif self.game_world.key == 'Right' and self.koord_x != self.Width - 1:
        self.koord_x += 1

    if self.koord_y % 2 == 0:
      if self.game_world.key == 'Home' and self.koord_x != 0 and self.koord_y != 0:
          self.koord_x -= 1
          self.koord_y -= 1  
      elif self.game_world.key == 'Prior' and self.koord_y != 0:
          self.koord_y -= 1

      if self.Height % 2 == 0:
         if self.game_world.key == 'End' and self.koord_x != 0:
             self.koord_x -= 1
             self.koord_y += 1
         elif self.game_world.key == 'Next':
             self.koord_y += 1
      elif self.Height % 2 == 1:
          if self.game_world.key == 'End' and self.koord_x != 0 and self.koord_y != self.Height-1:
             self.koord_y += 1
             self.koord_x -= 1
          elif self.game_world.key == 'Next' and self.koord_x != self.Width - 1 and self.koord_y != self.Height-1:
              self.koord_x += 1
              self.koord_y += 1
    elif self.koord_y % 2 == 1:
       if self.game_world.key == 'Home':
          self.koord_y -= 1  
       elif self.game_world.key == 'Prior' and self.koord_x != self.Width - 1:
          self.koord_y -= 1
          self.koord_x += 1

       if self.Height % 2 == 0:
         if self.game_world.key == 'End' and self.koord_y != self.Height-1:
             self.koord_y += 1
         elif self.game_world.key == 'Next' and self.koord_y != self.Height-1 and self.koord_x != self.Width-1:
             self.koord_y += 1
             self.koord_x += 1
       elif self.Height % 2 == 1:
          if self.game_world.key == 'End':
             self.koord_y += 1
             self.koord_x -= 1
          elif self.game_world.key == 'Next' and self.koord_x != self.Width - 1:
              self.koord_x += 1
              self.koord_y += 1


    for organisms in self.organism_vector:
        self.is_moved_board = False
        if self.is_reproduction_collision(organisms):
            break



   def Collision(self, organism):
    super().Collision(organism)
    if self.is_lost:
        messagebox.showinfo("End of the game", "You lost \nTo close the game, press \"OK\"")
        sys.exit(0)
