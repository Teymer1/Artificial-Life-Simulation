from Animal import Animal
import random

class Fox(Animal):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
        super().__init__(width, height, organism_vector, koord_x, koord_y)
        self.name = "Fox"
        self.index = 0
        self.power = 3
        self.initiative = 7
        self.color = "orange"

    def action(self, game_world, organism_vector):
        self.game_world = game_world
        self.organism_vector = organism_vector
        
        directions = [('Up', 0, -1), ('Down', 0, 1), ('Left', -1, 0), ('Right', 1, 0)]
        random.shuffle(directions)

        for name, dx, dy in directions:
            new_x = self.koord_x + dx
            new_y = self.koord_y + dy

            if 0 <= new_x < self.Width and 0 <= new_y < self.Height:
                strong_enemy_nearby = False
                for org in self.organism_vector:
                    if org.koord_x == new_x and org.koord_y == new_y and org.power > self.power:
                        strong_enemy_nearby = True
                        break
                
                if not strong_enemy_nearby:
                    for attr in ['WentUp', 'WentDown', 'WentLeft', 'WentRight']:
                        setattr(self, attr, False)
                    
                    self.koord_x = new_x
                    self.koord_y = new_y
                    setattr(self, f'Went{name}', True)
                    break 

        for organism in list(self.organism_vector):
            if self is not organism and self.koord_x == organism.koord_x and self.koord_y == organism.koord_y:
                if self.is_reproduction_collision(organism):
                    break