from Organism import Organism
import random
import tkinter.messagebox as messagebox
import sys

class Animal(Organism):
    def action(self, game_world, organism_vector):
        self.game_world = game_world
        self.organism_vector = organism_vector
        
        self.move_randomly()
        
        for organism in list(self.organism_vector):
            if self is not organism and self.koord_x == organism.koord_x and self.koord_y == organism.koord_y:
                if self.is_reproduction_collision(organism):
                    break

    def move_randomly(self, target_organism=None):
        target = target_organism or self
        for attr in ['WentUp', 'WentDown', 'WentLeft', 'WentRight']:
            setattr(target, attr, False)

        directions = [('Up', 0, -1), ('Down', 0, 1), ('Left', -1, 0), ('Right', 1, 0)]
        random.shuffle(directions)

        for name, dx, dy in directions:
            new_x = target.koord_x + dx
            new_y = target.koord_y + dy

            if 0 <= new_x < target.Width and 0 <= new_y < target.Height:
                target.koord_x = new_x
                target.koord_y = new_y
                setattr(target, f'Went{name}', True)
                return True
        return False

    def is_reproduction_collision(self, organism):
        if self.name == organism.name:
            if self.reproduction_break == 0:
                self.breeding(organism)
            else:
                self.move_randomly() 
            return True
        
        self.Collision(organism)
        return True

    def is_alzura_board(self, opponent):
        if getattr(opponent, 'alzura_board', False):
            Organism.results.append(f"{self.name} met Human, but Alzura Board reflected the attack!")
            self.move_randomly()
            return True
        return False

    def is_antelope_escape(self, opponent):
        if getattr(opponent, 'is_antelope', False):
            if random.randint(0, 1) == 0:  
                Organism.results.append(f"{opponent.name} escaped from the battle!")
                opponent.move_randomly()
                return True
        return False

    def Collision(self, organism):
        if self.is_alzura_board(organism):
            return

        if organism.index == 9:
            self.power += 3
            Organism.results.append(f"{self.name} ate Guarana and gained +3 power!")

        if self.power >= organism.power:
            if self.is_antelope_escape(organism):
                return
            
            is_turtle_defending = getattr(organism, 'is_success_attack', False)
            if is_turtle_defending and self.power < 5:
                Organism.results.append(f"{organism.name} reflected the attack of {self.name}")
                self.return_to_previous_position()
                return

            self.kill_organism(organism)
        else:
            self.is_lost = True
            Organism.results.append(f"{organism.name}({organism.power}) killed {self.name}({self.power})")


    def breeding(self, partner):
        from Fox import Fox
        from Wolf import Wolf
        from Sheep import Sheep
        from CyberSheep import CyberSheep
        from Antelope import Antelope
        from Turtle import Turtle
        classes = {0: Fox, 1: Wolf, 3: Sheep, 4: CyberSheep, 5: Antelope, 6: Turtle}
        
        if self.index in classes:
            child = classes[self.index](koord_x=self.koord_x, koord_y=self.koord_y, 
                                        width=self.Width, height=self.Height)
            self.organism_vector.append(child)
            Organism.results.append(f"New {self.name} was born at ({self.koord_x}, {self.koord_y})")
            
            self.return_to_previous_position()
            partner.reproduction_break = 30
            self.reproduction_break = 30

    def return_to_previous_position(self):
        if self.WentUp: self.koord_y += 1
        elif self.WentDown: self.koord_y -= 1
        elif self.WentLeft: self.koord_x += 1
        elif self.WentRight: self.koord_x -= 1

    def kill_organism(self, organism):
        Organism.results.append(f"{self.name}({self.power}) killed {organism.name}({organism.power})")
        if organism.name == "Human":
            messagebox.showinfo("Game over", "You lost!")
            sys.exit(0)
        if organism in self.organism_vector:
            self.organism_vector.remove(organism)



