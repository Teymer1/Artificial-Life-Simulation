from Organism import Organism
import random

class Plants(Organism):

  def action(self, game_world, organism_vector):
    self.game_world = game_world
    self.TriedUp = False
    self.TriedDown = False
    self.TriedLeft = False
    self.TriedRight = False
    koord_y_rozprzestrzenie = 0
    koord_x_rozprzestrzenie = 0
    random.seed()
    self.organism_vector = organism_vector
    is_spread = random.randint(0, 79)
    if is_spread == 7:
        from Dandelion import Dandelion
        from Grass import Grass
        from Guarana import Guarana
        from SosnowskyHogweed import SosnowskyHogweed
        from Wolfberries import Wolfberries
        is_free_space = 0
        direction = random.randint(1, 4)
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

            if direction == 1 and self.koord_y > 0:
                koord_y_rozprzestrzenie = self.koord_y - 1
                koord_x_rozprzestrzenie = self.koord_x
                for vector in organism_vector:
                    if (koord_x_rozprzestrzenie != vector.koord_x or koord_y_rozprzestrzenie != vector.koord_y):
                        is_free_space += 1
                if is_free_space == len(organism_vector):
                    executed = True
            elif direction == 2 and self.koord_x < self.Width - 1:
                koord_y_rozprzestrzenie = self.koord_y  
                koord_x_rozprzestrzenie = self.koord_x + 1
                for vector in organism_vector:
                    if (koord_x_rozprzestrzenie != vector.koord_x or koord_y_rozprzestrzenie != vector.koord_y):
                        is_free_space += 1
                if is_free_space == len(organism_vector):
                   executed = True
            elif direction == 3 and self.koord_y < self.Height - 1:
                koord_y_rozprzestrzenie = self.koord_y + 1  
                koord_x_rozprzestrzenie = self.koord_x
                for vector in organism_vector:
                    if (koord_x_rozprzestrzenie != vector.koord_x or koord_y_rozprzestrzenie != vector.koord_y):
                        is_free_space += 1
                if is_free_space == len(organism_vector):
                   executed = True
            elif direction == 4 and self.koord_x > 0:
                koord_y_rozprzestrzenie = self.koord_y  
                koord_x_rozprzestrzenie = self.koord_x - 1
                for vector in organism_vector:
                    if (koord_x_rozprzestrzenie != vector.koord_x or koord_y_rozprzestrzenie != vector.koord_y):
                        is_free_space += 1
                if is_free_space == len(organism_vector):
                   executed = True
            direction = random.randint(1, 4)

            if executed and (not self.TriedUp or not self.TriedDown or not self.TriedLeft or not self.TriedRight):
                if self.index == 7:
                    organism_vector.append(Grass(koord_x=koord_x_rozprzestrzenie, koord_y=koord_y_rozprzestrzenie, width=self.Width,height=self.Height))
                elif self.index == 8:
                    organism_vector.append(Dandelion(koord_x=koord_x_rozprzestrzenie, koord_y=koord_y_rozprzestrzenie,width=self.Width,height=self.Height))
                elif self.index == 9:
                    organism_vector.append(Guarana(koord_x=koord_x_rozprzestrzenie, koord_y=koord_y_rozprzestrzenie,width=self.Width,height=self.Height))
                elif self.index == 10:
                    organism_vector.append(Wolfberries(koord_x=koord_x_rozprzestrzenie, koord_y=koord_y_rozprzestrzenie,width=self.Width,height=self.Height))
                elif self.index == 11:
                    organism_vector.append(SosnowskyHogweed(koord_x=koord_x_rozprzestrzenie, koord_y=koord_y_rozprzestrzenie,width=self.Width,height=self.Height))

            if executed:
             Organism.results.append(f"{self.name}({self.koord_x},{self.koord_y}) sowed ({koord_x_rozprzestrzenie},{koord_y_rozprzestrzenie})")

            if self.TriedUp and self.TriedDown and self.TriedLeft and self.TriedRight:
                executed = True

    
  def Collision(self):
        pass

  def breeding(self):
        pass



