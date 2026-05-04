import tkinter as tk
from tkinter import font
from AddingOrganism import AddingOrganism

class CreatureSelectionPanel(tk.Frame):
 def __init__(self, organism_vector, cursor_x, cursor_y, Width, Height):
   self.organism_vector = organism_vector
   self.cursor_x = cursor_x
   self.cursor_y = cursor_y
   self.Width = Width
   self.Height = Height
   self.window = tk.Tk()
   self.window.geometry("670x430")
   self.window.title("Adding an entity")
   self.window.configure(bg="cyan")

   custom_font = font.Font(size=12)
 
   container = tk.Frame(self.window)
   container.pack(expand=True, pady=self.window.winfo_height() // 2)
   container.configure(bg="cyan")

   Creature = tk.Label(container, text="Enter the creature index (0,1, 3 to 11)", font=custom_font, bg="cyan")
   Creature.grid(row=0, column=1, sticky="w")

   self.Index = tk.Entry(container)
   self.Index.grid(row=1, column=1, pady=(0, 10), ipadx=30, sticky="w")

   submit_button = tk.Button(container, text="Continue", command=lambda: self.entry(), font=custom_font)
   submit_button.grid(row=2, column=1, sticky="w")

   panelIndex0 = tk.Label(container, text="0 - Fox", font=custom_font, bg="cyan")
   panelIndex0.grid(row=0, column=0, sticky="w")
   
   panelIndex1 = tk.Label(container, text="1 - Wolf", font=custom_font, bg="cyan")
   panelIndex1.grid(row=1, column=0, sticky="w")
   
   panelIndex3 = tk.Label(container, text="3 - Sheep", font=custom_font, bg="cyan")
   panelIndex3.grid(row=2, column=0, sticky="w")
   
   panelIndex4 = tk.Label(container, text="4 - Cyber Sheep", font=custom_font, bg="cyan")
   panelIndex4.grid(row=3, column=0, sticky="w")

   panelIndex5 = tk.Label(container, text="5 - Antelope", font=custom_font, bg="cyan")
   panelIndex5.grid(row=4, column=0, sticky="w")
   
   panelIndex6 = tk.Label(container, text="6 - Turtle", font=custom_font, bg="cyan")
   panelIndex6.grid(row=5, column=0, sticky="w")
   
   panelIndex7 = tk.Label(container, text="7 - Grass", font=custom_font, bg="cyan")
   panelIndex7.grid(row=6, column=0, sticky="w")
   
   panelIndex8 = tk.Label(container, text="8 - Dandelion", font=custom_font, bg="cyan")
   panelIndex8.grid(row=7, column=0, sticky="w")
   
   panelIndex9 = tk.Label(container, text="9 - Guarana", font=custom_font, bg="cyan")
   panelIndex9.grid(row=8, column=0, sticky="w")
   
   panelIndex10 = tk.Label(container, text="10 - Wolfberries", font=custom_font, bg="cyan")
   panelIndex10.grid(row=9, column=0, sticky="w")
   
   panelIndex11 = tk.Label(container, text="11 - SosnowskyHogweed", font=custom_font, bg="cyan")
   panelIndex11.grid(row=10, column=0, sticky="w")

   self.window.mainloop()
        

 def entry(self):
    self.creature_index = int(self.Index.get())
    if self.creature_index != "" and self.creature_index != 2 and self.creature_index <= 11:
         AddingOrganism(self.organism_vector, self.creature_index, self.cursor_x, self.cursor_y, self.Width, self.Height)
         self.window.destroy()

