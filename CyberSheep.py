from Animal import Animal
import random

class CyberSheep(Animal):
   def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
     super().__init__(width, height, organism_vector, koord_x, koord_y)
     self.name = "Cyber Sheep";
     self.index = 4;
     self.power = 11;
     self.initiative = 4;
     self.color = "gold"

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

    self.GetClosestHogweed()

    if self.ClosestHogweed is not None:
        diff_x = self.ClosestHogweed.koord_x - self.koord_x
        diff_y = self.ClosestHogweed.koord_y - self.koord_y

        if abs(diff_x) > abs(diff_y):
            if diff_x > 0:
                self.koord_x += 1  # Move right
                self.WentRight = True
            else:
                self.koord_x -= 1  # Move left
                self.WentLeft = True
        else:
            if diff_y > 0:
                self.koord_y += 1  # Move down
                self.WentDown = True
            else:
                self.koord_y -= 1  # Move up
                self.WentUp = True
    else:
        super().action(game_world,organism_vector)
    for organism in self.organism_vector:
        self.is_moved_board = False
        if self.is_reproduction_collision(organism):
            break


   def GetClosestHogweed(self):
    Hogweed = float('inf')
    self.ClosestHogweed = None
    for organism in self.organism_vector:
        if organism.cybersheep_goal:
            distance = abs(self.koord_x - organism.koord_x) + abs(self.koord_y - organism.koord_y)
            if distance < Hogweed:
                Hogweed = distance
                self.ClosestHogweed = organism

  