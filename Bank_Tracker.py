from tkinter import *
import tkinter as tk

root = Tk()

# specify size of window.
root.geometry("500x250")

# Create text widget and specify size.
T = Text(root, height = 10, width = 52)

# Create label
l = Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))

Fact = """A man can be arrested in
Italy for wearing a skirt in public."""

l.pack()
T.pack()

# Insert The Fact.
T.insert(tk.END, Fact)

root.mainloop()
