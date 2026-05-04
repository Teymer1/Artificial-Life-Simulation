import tkinter as EntryPanel
from tkinter import font

def entry():
    global width
    global height
    width = width_entry.get()
    height = height_entry.get()
    if width != "" and height != "":
        window.destroy()

window = EntryPanel.Tk()
window.geometry("320x180")
window.title("Enter size")
window.configure(bg="cyan")

custom_font = font.Font(size=12)

container = EntryPanel.Frame(window)
container.pack(expand=True, pady=window.winfo_height() // 2)
container.configure(bg="cyan")

width_label = EntryPanel.Label(container, text="Width:", font=custom_font, bg="cyan")
width_label.pack()

width_entry = EntryPanel.Entry(container)
width_entry.pack(pady=(0, 10), ipadx=10)

height_label = EntryPanel.Label(container, text="Height:", font=custom_font, bg="cyan")
height_label.pack()

height_entry = EntryPanel.Entry(container)
height_entry.pack(pady=(0, 10), ipadx=10)

submit_button = EntryPanel.Button(container, text="Continue", command=entry, font=custom_font)
submit_button.pack()

window.mainloop()
