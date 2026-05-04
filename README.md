# Artificial Life Simulation (Python)

A grid-based ecosystem simulation developed as a university project. The world consists of various organisms (animals and plants) that interact, reproduce, and fight for survival based on specific attributes like power and initiative.

## 📧 Project Overview
- **Language:** Python
- **GUI Library:** Tkinter
- **Core Concepts:** Object-Oriented Programming (OOP), Inheritance, Polymorphism, Collision Detection, and State Management.

## 🛠 Features
- **Grid Systems:** Supports both **Square** and **Hexagonal** world layouts.
- **Dynamic Ecosystem:** Organisms have unique behaviors (e.g., Turtle's defense, Antelope's escape, Human's special skill).
- **Turn-based Logic:** Movement and actions are determined by an initiative system.
- **Save/Load System:** Ability to save the current world state to a file using `pickle`.
- **Manual Intervention:** A "Creator Mode" to manually add organisms to the board.

## 🧬 Organisms & Mechanics
The simulation includes specialized classes:
- **Human:** Controlled by the player with a special skill "Alzura Board" (invincibility).
- **Animals:** Wolf, Sheep, Fox, Turtle, Antelope, Cyber Sheep.
- **Plants:** Grass, Dandelion, Guarana, Wolfberries, Sosnowsky's Hogweed.

### Special Rules implemented:
- **Reproduction:** Organisms can breed when two of the same species meet.
- **Collision Logic:** Specific interactions based on power levels (e.g., the Turtle repels attackers with power < 5).

## 🎮 Controls
- **Arrows/Numpad:** Move the Human or navigate the cursor.
- **Space:** Proceed to the next turn.
- **R:** Activate Human special skill.
- **S:** Save game state.
- **U/Y:** Open the creation panel to add new life forms.
