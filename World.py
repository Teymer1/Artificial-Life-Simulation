import tkinter as tk
from tkinter import font
from CreateOrganism import CreateOrganism
import sys
from CreatureSelectionPanel import CreatureSelectionPanel
import pickle
from Fox import Fox
from Wolf import Wolf
from Sheep import Sheep
from Human import Human
from CyberSheep import CyberSheep
from Antelope import Antelope
from Turtle import Turtle
from Dandelion import Dandelion
from Grass import Grass
from Guarana import Guarana
from SosnowskyHogweed import SosnowskyHogweed
from Wolfberries import Wolfberries

class World:
 organism_vector = []
 vector_for_history = []
 hex_style = False
 board_type = 0
 size_x = 0
 size_y = 0

 def __init__(self, width, height):
    self.Width=width
    self.Height=height
    self.is_activated_cursor = False
    self.cursorX = 0
    self.cursorY = 0
    self.end_of_turn = False
    self.nr_tury = 1

    self.new_window = tk.Tk()
    self.new_window.geometry("1200x600")
    self.new_window.title("Game World")
    self.new_window.configure(bg="lightgrey")
    self.fontsize = font.Font(size=12)
    self.skill_var = tk.StringVar()

    self.PLANSZA_X = 10  # start of the board
    self.PLANSZA_Y = 15

    self.WINDOW_HEIGHT = 600    # Size of game
    self.WINDOW_WIDTH = 1200

    self.BOARD_HEIGHT=self.BOARD_WIDTH=int(self.WINDOW_HEIGHT*3/4)
    self.color = "white"
    self.CREATURE_WIDTH = int(self.BOARD_WIDTH/width)
    self.CREATURE_HEIGHT = int(self.BOARD_HEIGHT/height)

    self.size_x = int(self.BOARD_WIDTH/self.Width)
    self.size_y = int(self.BOARD_HEIGHT/self.Height)

    self.canvas = tk.Canvas(self.new_window, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT, bg="lightgrey")
    self.canvas.config(highlightbackground="lightgrey")
    self.canvas.place(x=self.PLANSZA_X, y=self.PLANSZA_Y)

    StworzoneOrganism = CreateOrganism(int(self.Width), int(self.Height))
    self.organism_vector = StworzoneOrganism.getorganism_vector()
    self.vector_for_history = self.organism_vector.copy()

    empty_board = tk.Button(self.new_window, text="Empty board", font=("Arial", 12), command=self.Pustaplansza)
    empty_board.place(x=350, y=self.BOARD_HEIGHT+70)

    self.draw_history_board()
    self.draw_animals()
    self.draw_results()

    self.new_window.bind("<Key>", self.keyPressed)
    self.new_window.mainloop()
  

 def Pustaplansza(self):
    for organism in self.organism_vector:
        if organism.index == 2:
            czlowiek_x = organism.koord_x
            czlowiek_y = organism.koord_y
            break

    self.organism_vector.clear()
    self.organism_vector.append(Human(koord_x=czlowiek_x, koord_y=czlowiek_y, width=self.Width,height=self.Height))

    if self.hex_style == False:
      self.draw_history_board()
      self.draw_animals()
      self.draw_results()
    else:
       self.canvas.delete("all")
       self.draw_history_board()
       self.draw_hex_board()
       self.draw_results()


 def draw_history_board(self):
    self.canvas.delete("all")

    if self.hex_style == False:
     arrows_field = tk.Label(self.new_window, text="Arrows - Moving", font=self.fontsize, bg="lightgrey")
     arrows_field.place(x=self.BOARD_WIDTH+self.PLANSZA_X*3, y=20)

    if self.hex_style == True:
        arrows_field = tk.Label(self.new_window, text="NumPad(1,4,7,9,6,3) - Moving", font=self.fontsize, bg="lightgrey")
        arrows_field.place(x=self.BOARD_WIDTH+self.PLANSZA_X*3, y=20)

    escape_field = tk.Label(self.new_window, text="Escape - Game over", font=self.fontsize, bg="lightgrey")
    escape_field.place(x=self.BOARD_WIDTH+self.PLANSZA_X*3, y=45)

    new_tour_field = tk.Label(self.new_window, text="Space - New round", font=self.fontsize, bg="lightgrey")
    new_tour_field.place(x=self.BOARD_WIDTH+self.PLANSZA_X*3, y=70)

    skill_field = tk.Label(self.new_window, text="R - Skill", font=self.fontsize, bg="lightgrey")
    skill_field.place(x=self.BOARD_WIDTH+self.PLANSZA_X*3, y=95)

    save_game_field = tk.Label(self.new_window, text="S - Save game", font=self.fontsize, bg="lightgrey")
    save_game_field.place(x=self.BOARD_WIDTH+self.PLANSZA_X*3, y=120)

    start_cursor = tk.Label(self.new_window, text="U - Activate cursor", font=self.fontsize, bg="lightgrey")
    start_cursor.place(x=self.BOARD_WIDTH+self.PLANSZA_X*3, y=145)

    DodacorganismPole = tk.Label(self.new_window, text="Y - Add a new organism", font=self.fontsize, bg="lightgrey")
    DodacorganismPole.place(x=self.BOARD_WIDTH+self.PLANSZA_X*3, y=170)

    Tura = tk.Label(self.new_window, text="Tour number : " + str(self.nr_tury), font=self.fontsize, bg="lightgrey")
    Tura.place(x=250, y=2)

    offset = 0
    used_names = set()  

    if self.hex_style == False:
     self.canvas.create_rectangle(self.PLANSZA_X, self.PLANSZA_Y, self.PLANSZA_X + self.BOARD_WIDTH, self.PLANSZA_Y + self.BOARD_HEIGHT, fill=self.color)

    elif self.hex_style == True:
            x = self.BOARD_WIDTH + 30
            y = 170

    for organism in self.vector_for_history:
       name = organism.name
       if name not in used_names:  
        used_names.add(name)  
        if self.hex_style == False:
          y = 200 + offset
          self.canvas.create_text(self.BOARD_WIDTH + 40, y-5, text=" - " + name, font=self.fontsize, anchor="w")
          self.canvas.create_rectangle(self.BOARD_WIDTH + 20, y - 12, self.BOARD_WIDTH + 20 + 15, y - 12 + 15, fill=organism.color)
          offset += 20

        elif self.hex_style == True:
            Wiercholki = [
                x, y-13,                                                   
                x + int(20*0.5), y-13,                             
                x + int(20*0.75), y + int(20*0.5)-13,       
                x + int(20*0.5), y + 20-13,                
                x, y + 20-13,                                         
                x - int(20*0.25), y + int(20*0.5)-13       
               ] 
            self.canvas.create_polygon(Wiercholki, fill=organism.color)
            self.canvas.create_text(self.BOARD_WIDTH + 45, y-5, text=" - " + name, font=self.fontsize, anchor="w")
            y += 20+5


    read_button = tk.Button(self.new_window, text="Load the game", font=("Arial", 12), command=self.load_game)
    read_button.place(x=90, y=self.BOARD_HEIGHT+70)
    change_fields = tk.Button(self.new_window, text="Change field", font=("Arial", 12), command=self.BoardType)
    change_fields.place(x=220, y=self.BOARD_HEIGHT+70)


 def draw_animals(self):
     for organism in self.organism_vector:
          self.canvas.create_rectangle(self.PLANSZA_X+self.CREATURE_WIDTH*organism.koord_x, self.PLANSZA_Y+self.CREATURE_HEIGHT*organism.koord_y, self.PLANSZA_X+self.CREATURE_WIDTH*(organism.koord_x+1), self.PLANSZA_Y+self.CREATURE_HEIGHT*(organism.koord_y+1), fill=organism.color)
     if self.is_activated_cursor:
       self.canvas.create_rectangle(self.PLANSZA_X + self.CREATURE_WIDTH * self.cursorX, self.PLANSZA_Y + self.CREATURE_HEIGHT * self.cursorY, self.PLANSZA_X + self.CREATURE_WIDTH * (self.cursorX + 1), self.PLANSZA_Y + self.CREATURE_HEIGHT * (self.cursorY + 1), fill="thistle1")


 def draw_results(self):
    for organism in self.organism_vector:
        if organism.skill_cooldown != None:
            if organism.skill_cooldown == 0:
                text = "You can activate the skill (Alzura Board)"
                break
            elif organism.skill_cooldown > 5:
                text = f"Skill (Alzura Board) activated for another {organism.skill_cooldown - 5} turns"
                break
            elif organism.skill_cooldown <= 5:
                text = f"Skill (Alzura Board) activated for another {organism.skill_cooldown} turns"
                break
    Skill = tk.Label(self.new_window, textvariable=self.skill_var, font=self.fontsize, bg="lightgrey")
    self.skill_var.set(text)
    Skill.place(x=50, y=self.BOARD_HEIGHT+40)

    self.results_y = self.PLANSZA_Y*5
    for wynik in self.organism_vector[0].results:
     self.canvas.create_text(self.BOARD_WIDTH + 220, self.results_y, text=wynik, font=self.fontsize, anchor="w")
     self.results_y += 25
    self.organism_vector[0].results.clear()
    
    
 def choose_being(self):
    if self.is_free_space():
        WyborIstot = CreatureSelectionPanel(self.organism_vector,self.cursorX,self.cursorY, self.Width, self.Height)
       


 def is_free_space(self):
    wolne = 0
    for org in self.organism_vector:
        if self.cursorX != org.koord_x or self.cursorY != org.koord_y:
            wolne += 1
    return wolne == len(self.organism_vector)



 def keyPressed(self, event):
        self.key = event.keysym
        if self.key == 'u':
           if self.hex_style == False:
                self.is_activated_cursor = not self.is_activated_cursor
                self.draw_history_board()
                self.draw_results()
                self.draw_animals()
           elif self.hex_style == True:
                self.is_activated_cursor = not self.is_activated_cursor
                self.draw_history_board()
                self.draw_hex_board()
                self.draw_results()

        if self.is_activated_cursor:
            if self.key == 'y':
                self.choose_being()

            self.moving_cursor()
            if self.hex_style == False:
                self.canvas.delete("all")
                self.draw_history_board()
                self.draw_results()
                self.draw_animals()
            elif self.hex_style == True:
                self.draw_history_board()
                self.draw_hex_board()
                self.draw_results()

        if self.is_activated_cursor == False:
            for organism in self.organism_vector:
              if organism.index == 2:
               if self.key == 'r':
                   if organism.skill_cooldown == 0:
                    organism.skill_cooldown = 11
                    organism.alzura_board = True
               if organism.skill_cooldown == 5:
                    organism.alzura_board = False
               break
            if (self.key == 'Up' or self.key == 'Down' or self.key == 'Left' or self.key == 'Right') and not self.end_of_turn and not self.hex_style:
                self.main_game()
                self.canvas.delete("all")
                self.draw_history_board()
                self.draw_animals()
                self.draw_results()

            if (self.key == 'Prior' or self.key == 'Home' or self.key == 'Left' or self.key == 'End' or self.key == 'Next' or self.key == 'Right') and not self.end_of_turn and self.hex_style:
                self.main_game()
                self.draw_history_board()
                self.draw_hex_board()
                self.draw_results()

            if self.key == 'space' and self.end_of_turn:
              self.end_of_turn = False
        if self.key == 'Escape':
             sys.exit(0)
        if self.key == 's':
            self.save_game()


 def moving_cursor(self):
       if self.key == 'Up' and self.cursorY > 0:
                self.cursorY -= 1
       elif self.key == 'Down' and self.cursorY < self.Height - 1:
                self.cursorY += 1
       elif self.key == 'Left' and self.cursorX > 0:
                self.cursorX -= 1
       elif self.key == 'Right' and self.cursorX < self.Width - 1:
                self.cursorX += 1
       if self.hex_style == True:
               if self.cursorY % 2 == 0:
                 if self.key == 'Home' and self.cursorX != 0 and self.cursorY != 0:
                   self.cursorX -= 1
                   self.cursorY -= 1  
                 elif self.key == 'Prior' and self.cursorY != 0:
                   self.cursorY -= 1
                 if self.Height % 2 == 0:
                    if self.key == 'End' and self.cursorX != 0:
                       self.cursorX -= 1
                       self.cursorY += 1
                    elif self.key == 'Next':
                       self.cursorY += 1
                 elif self.Height % 2 == 1:
                     if self.key == 'End' and self.cursorX != 0 and self.cursorY != self.Height-1:
                        self.cursorY += 1
                        self.cursorX -= 1
                     elif self.key == 'Next' and self.cursorX != self.Width - 1 and self.cursorY != self.Height-1:
                        self.cursorX += 1
                        self.cursorY += 1
               elif self.cursorY % 2 == 1:
                  if self.key == 'Home':
                     self.cursorY -= 1  
                  elif self.key == 'Prior' and self.cursorX != self.Width - 1:
                      self.cursorY -= 1
                      self.cursorX += 1
                  if self.Height % 2 == 0:
                    if self.key == 'End' and self.cursorY != self.Height-1:
                      self.cursorY += 1
                    elif self.key == 'Next' and self.cursorY != self.Height-1 and self.cursorX != self.Width-1:
                       self.cursorY += 1
                       self.cursorX += 1
                  elif self.Height % 2 == 1:
                       if self.key == 'End':
                         self.cursorY += 1
                         self.cursorX -= 1
                       elif self.key == 'Next' and self.cursorX != self.Width - 1:
                          self.cursorX += 1
                          self.cursorY += 1

       if self.key == 'space':
              self.is_activated_cursor = False
              self.organism_vector = sorted(self.organism_vector, key=lambda x: x.initiative, reverse=True)


 def main_game(self):
    human = next((o for o in self.organism_vector if o.index == 2), None)
    
    if human:
        success = human.action(self, self.organism_vector)
        if not success:
            self.end_of_turn = False
            return 

    self.end_of_turn = True
    
    for organism in list(self.organism_vector):
        if organism.index == 2: 
            continue
            
        if not organism.is_lost:
            organism.action(self, self.organism_vector)
            
    self.organism_vector = [o for o in self.organism_vector if not o.is_lost]
            
    for organism in self.organism_vector:
        if organism.index == 2:
            if organism.skill_cooldown > 0:
                organism.skill_cooldown -= 1
    
    self.nr_tury += 1
    self.organism_vector = sorted(self.organism_vector, key=lambda x: x.initiative, reverse=True)


 def save_game(self):
    lista_organismow = []
    for organism in self.organism_vector:
        organism_dict = {
            "name": organism.name,
            "index": organism.index,
            "power": organism.power,
            "initiative": organism.initiative,
            "color": organism.color,
            "koord_x": organism.koord_x,
            "koord_y": organism.koord_y,
            "Width": organism.Width,
            "Height": organism.Height,
            "cybersheep_goal": organism.cybersheep_goal,
            "is_success_attack": organism.is_success_attack,
            "is_antelope": organism.is_antelope,
            "alzura_board": organism.alzura_board,
            "reproduction_break": organism.reproduction_break,
            "skill_cooldown": organism.skill_cooldown
        }
        lista_organismow.append(organism_dict)

    with open("Save.txt", "wb") as file:
        pickle.dump(lista_organismow, file)
        print("Created file")


 def load_game(self):
    with open("Save.txt", "rb") as file:
        lista_organismow = pickle.load(file)
    
    self.organism_vector = []  
    
    for organism_dict in lista_organismow:
        if organism_dict["name"] == "Fox":
            organism = Fox()
        elif organism_dict["name"] == "Wolf":
            organism = Wolf()
        elif organism_dict["name"] == "Human":
            organism = Human()
        elif organism_dict["name"] == "Sheep":
            organism = Sheep()
        elif organism_dict["name"] == "Cyber Sheep":
            organism = CyberSheep()
        elif organism_dict["name"] == "Turtle":
            organism = Turtle()
        elif organism_dict["name"] == "Antelope":
            organism = Antelope()
        elif organism_dict["name"] == "Dandelion":
            organism = Dandelion()
        elif organism_dict["name"] == "Grass":
            organism = Grass()
        elif organism_dict["name"] == "Guarana":
            organism = Guarana()
        elif organism_dict["name"] == "Wolfberries":
            organism = Wolfberries()
        elif organism_dict["name"] == "SosnowskyHogweed":
            organism = SosnowskyHogweed()
        else:
            continue  
        
        organism.name = organism_dict["name"]
        organism.index = organism_dict["index"]
        organism.power = organism_dict["power"]
        organism.initiative = organism_dict["initiative"]
        organism.color = organism_dict["color"]
        organism.koord_x = organism_dict["koord_x"]
        organism.koord_y = organism_dict["koord_y"]
        organism.Width = organism_dict["Width"]
        organism.Height = organism_dict["Height"]
        organism.cybersheep_goal = organism_dict["cybersheep_goal"]
        organism.is_success_attack = organism_dict["is_success_attack"]
        organism.is_antelope = organism_dict["is_antelope"]
        organism.alzura_board = organism_dict["alzura_board"]
        organism.reproduction_break = organism_dict["reproduction_break"]
        organism.skill_cooldown = organism_dict["skill_cooldown"]
        
        self.organism_vector.append(organism)  

    self.Width = organism_dict["Width"]
    self.Height = organism_dict["Height"]
    self.CREATURE_WIDTH = int(self.BOARD_WIDTH/self.Width)
    self.CREATURE_HEIGHT = int(self.BOARD_HEIGHT/self.Height)

    self.size_x = int(self.BOARD_WIDTH/self.Width)
    self.size_y = int(self.BOARD_HEIGHT/self.Height)
    if self.hex_style == False:
       self.canvas.delete("all")
       self.draw_history_board()
       self.draw_results()
       self.draw_animals()
    else:
       self.draw_history_board()
       self.draw_hex_board()
       self.draw_results()


 def BoardType(self):
      self.board_type += 1
      if self.board_type % 2 == 1:
          self.draw_hex_board()
      elif self.board_type % 2 == 0:
            self.hex_style = False
            self.draw_history_board()
            self.draw_animals()
            self.draw_results()


 def draw_hex_board(self):
    self.hex_style = True
    self.canvas.delete("all")
    self.draw_history_board()

    nr_line = 0

    for i in range(self.Height):
        koord_po_x = 1
        if nr_line % 2 == 0:
                 x = self.PLANSZA_X + int(self.size_x*0.25)*koord_po_x
        elif nr_line % 2 == 1:
                 x = self.PLANSZA_X + int(self.size_x*0.75)*koord_po_x
        y = self.PLANSZA_Y + self.size_y*nr_line
        for j in range(self.Width):

             Wiercholki = [
                x, y,                                                     
                x + int(self.size_x*0.5), y,                              
                x + int(self.size_x*0.75), y + int(self.size_y*0.5),       
                x + int(self.size_x*0.5), y + self.size_y,                
                x, y + self.size_y,                                        
                x - int(self.size_x*0.25), y + int(self.size_y*0.5)       
               ] 
             self.canvas.create_polygon(Wiercholki, fill="white")
             koord_po_x += 1
             x += self.size_x
        nr_line += 1

    self.DrawHexAnimals()


 def DrawHexAnimals(self):
    for organism in self.organism_vector:
        if organism.koord_y % 2 == 0:
                 x = self.PLANSZA_X + int(self.size_x*0.25)+organism.koord_x*self.size_x
        elif organism.koord_y % 2 == 1:
                 x = self.PLANSZA_X + int(self.size_x*0.75)+organism.koord_x*self.size_x
        y = self.PLANSZA_Y + self.size_y*organism.koord_y

        Wiercholki = [
                x, y,                                                      
                x + int(self.size_x*0.5), y,                              
                x + int(self.size_x*0.75), y + int(self.size_y*0.5),      
                x + int(self.size_x*0.5), y + self.size_y,                
                x, y + self.size_y,                                          
                x - int(self.size_x*0.25), y + int(self.size_y*0.5)       
              ] 

        self.canvas.create_polygon(Wiercholki, fill=organism.color)

    if self.is_activated_cursor:
       if self.cursorY % 2 == 0:
                 x = self.PLANSZA_X + int(self.size_x*0.25)+self.cursorX*self.size_x
       elif self.cursorY % 2 == 1:
                 x = self.PLANSZA_X + int(self.size_x*0.75)+self.cursorX*self.size_x
       y = self.PLANSZA_Y + self.size_y*self.cursorY
       Cursor = [
                x, y,                                                      
                x + int(self.size_x*0.5), y,                              
                x + int(self.size_x*0.75), y + int(self.size_y*0.5),       
                x + int(self.size_x*0.5), y + self.size_y,                
                x, y + self.size_y,                                         
                x - int(self.size_x*0.25), y + int(self.size_y*0.5)       
               ] 
       self.canvas.create_polygon(Cursor, fill="thistle1")


        
