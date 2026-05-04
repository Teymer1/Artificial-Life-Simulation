import random
from abc import ABC, abstractmethod

class Organism(ABC):
    organism_vector = []
    name = None
    index = None
    power = None
    initiative = None
    color = None
    koord_x = None
    koord_y = None
    Width = None
    Height = None
    is_lost = False
    cybersheep_goal = False
    is_success_attack = False
    is_antelope = False
    alzura_board = False
    game_world = None
    WentUp = False
    WentDown = False
    WentLeft = False
    WentRight = False
    TriedUp = False
    TriedDown = False
    TriedLeft = False
    TriedRight = False
    results = [] 
    reproduction_break = 0
    skill_cooldown = None

    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
       rand = random.Random()
       if koord_x is not None and koord_y is not None and width is not None and height is not None and organism_vector is None:
          self.koord_x = koord_x
          self.koord_y = koord_y
          self.Width = width
          self.Height = height
          self.reproduction_break = 30
       elif width is not None and height is not None and organism_vector is not None and koord_x is None and koord_y is None:
          self.Width = width
          self.Height = height
          self.koord_y = rand.randint(0, height - 1)
          self.koord_x = rand.randint(0, width - 1)
          self.reproduction_break = 30
          for org in organism_vector:
            if self.koord_y == org.koord_y and self.koord_x == org.koord_x:
                self.koord_y = rand.randint(0, height - 1)
                self.koord_x = rand.randint(0, width - 1)
       elif width is None and height is None and organism_vector is None and koord_x is None and koord_y is None:
           pass


    def __str__(self):
      return f"{self.name}(power: {self.power}, initiative: {self.initiative}, id: {self.index}) in position ({self.koord_x}, {self.koord_y})"
    
    @abstractmethod
    def action(self, game_world, organism_vector):
        pass
    
    @abstractmethod
    def Collision(self):
        pass
    
    @abstractmethod
    def breeding(self):
        pass






