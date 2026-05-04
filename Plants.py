import random
from Organism import Organism

class Plants(Organism):

    def action(self, game_world, organism_vector):
        self.game_world = game_world
        if random.randint(0, 79) != 7:
            return

        directions = [
            (0, -1),  # Up
            (1, 0),   # Right
            (0, 1),   # Down
            (-1, 0)   # Left
        ]
        random.shuffle(directions) 

        for dx, dy in directions:
            new_x = self.koord_x + dx
            new_y = self.koord_y + dy

            if 0 <= new_x < self.Width and 0 <= new_y < self.Height:
                
                is_free = True
                for org in organism_vector:
                    if org.koord_x == new_x and org.koord_y == new_y:
                        is_free = False
                        break
                
                if is_free:
                    self._create_new_plant(new_x, new_y, organism_vector)
                    Organism.results.append(
                        f"{self.name}({self.koord_x},{self.koord_y}) sowed ({new_x},{new_y})"
                    )
                    break 

    def _create_new_plant(self, x, y, organism_vector):
        from Dandelion import Dandelion
        from Grass import Grass
        from Guarana import Guarana
        from SosnowskyHogweed import SosnowskyHogweed
        from Wolfberries import Wolfberries

        plant_map = {
            7: Grass,
            8: Dandelion,
            9: Guarana,
            10: Wolfberries,
            11: SosnowskyHogweed
        }

        plant_class = plant_map.get(self.index)
        if plant_class:
            organism_vector.append(plant_class(
                koord_x=x, 
                koord_y=y, 
                width=self.Width, 
                height=self.Height
            ))

    def Collision(self, organism=None):
        pass

    def breeding(self):
        pass