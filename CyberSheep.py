from Animal import Animal

class CyberSheep(Animal):
    def __init__(self, width=None, height=None, organism_vector=None, koord_x=None, koord_y=None):
        super().__init__(width, height, organism_vector, koord_x, koord_y)
        self.name = "Cyber Sheep"
        self.index = 4
        self.power = 11
        self.initiative = 4
        self.color = "gold"
        self.ClosestHogweed = None

    def action(self, game_world, organism_vector):
        self.game_world = game_world
        self.organism_vector = organism_vector

        for attr in ['WentUp', 'WentDown', 'WentLeft', 'WentRight']:
            setattr(self, attr, False)

        self.find_closest_hogweed()

        if self.ClosestHogweed is not None:
            self.move_towards_target()
        else:
            super().action(game_world, organism_vector)
            return  

        for organism in list(self.organism_vector):
            if self is not organism and self.koord_x == organism.koord_x and self.koord_y == organism.koord_y:
                if self.is_reproduction_collision(organism):
                    break

    def find_closest_hogweed(self):
        min_distance = float('inf')
        self.ClosestHogweed = None
        
        for organism in self.organism_vector:
            if getattr(organism, 'cybersheep_goal', False) and not getattr(organism, 'is_lost', False):
                distance = abs(self.koord_x - organism.koord_x) + abs(self.koord_y - organism.koord_y)
                if distance < min_distance:
                    min_distance = distance
                    self.ClosestHogweed = organism

    def move_towards_target(self):
        diff_x = self.ClosestHogweed.koord_x - self.koord_x
        diff_y = self.ClosestHogweed.koord_y - self.koord_y

        if abs(diff_x) >= abs(diff_y):
            if diff_x > 0:
                self.koord_x += 1
                self.WentRight = True
            else:
                self.koord_x -= 1
                self.WentLeft = True
        else:
            if diff_y > 0:
                self.koord_y += 1
                self.WentDown = True
            else:
                self.koord_y -= 1
                self.WentUp = True

