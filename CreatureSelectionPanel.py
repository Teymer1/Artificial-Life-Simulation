import tkinter as tk
from tkinter import font, messagebox
from AddingOrganism import AddingOrganism

class CreatureSelectionPanel:
    def __init__(self, organism_vector, cursor_x, cursor_y, width, height):
        self.organism_vector = organism_vector
        self.cursor_x = cursor_x
        self.cursor_y = cursor_y
        self.width = width
        self.height = height

        self.window = tk.Toplevel()
        self.window.title("Adding an entity")
        self.window.geometry("450x500")
        self.window.configure(bg="#e0f7fa") 
        
        self.window.grab_set() 

        self.custom_font = font.Font(size=11)
        
        self.creatures = {
            0: "Fox", 1: "Wolf", 3: "Sheep", 4: "Cyber Sheep",
            5: "Antelope", 6: "Turtle", 7: "Grass", 8: "Dandelion",
            9: "Guarana", 10: "Wolfberries", 11: "Sosnowsky Hogweed"
        }

        self._setup_ui()

    def _setup_ui(self):
        list_frame = tk.Frame(self.window, bg="#e0f7fa")
        list_frame.pack(side="left", padx=20, fill="y")

        tk.Label(list_frame, text="Available indices:", font=(None, 12, "bold"), bg="#e0f7fa").pack(pady=10)

        for idx, name in self.creatures.items():
            tk.Label(list_frame, text=f"{idx} - {name}", font=self.custom_font, bg="#e0f7fa", anchor="w").pack(fill="x")

        input_frame = tk.Frame(self.window, bg="#e0f7fa")
        input_frame.pack(side="right", padx=20, expand=True)

        tk.Label(input_frame, text="Enter index:", font=self.custom_font, bg="#e0f7fa").pack()
        
        self.index_entry = tk.Entry(input_frame, font=self.custom_font)
        self.index_entry.pack(pady=10)
        self.index_entry.focus_set() 

        tk.Button(input_frame, text="Add Organism", command=self.confirm_entry, 
                  font=self.custom_font, bg="#b2ebf2", padx=10, pady=5).pack(pady=20)

    def confirm_entry(self):
        try:
            entry_val = self.index_entry.get()
            if not entry_val:
                return

            idx = int(entry_val)

            if idx in self.creatures:
                AddingOrganism(self.organism_vector, idx, self.cursor_x, 
                               self.cursor_y, self.width, self.height)
                self.window.destroy()
            else:
                messagebox.showwarning("Wrong Index", "Please enter an index from the list (0-11, except 2)")
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number (integer)")