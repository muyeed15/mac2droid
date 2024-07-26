from tkinter import *
from tkinter import ttk
import os

root = Tk()

root.geometry("640x480")

e1 = ttk.Entry(root)
e1.pack()

e2 = ttk.Entry(root)
e2.pack()

def pair(e1, e2):
    os.system(f"adb pair {e1} {e2}")

b1 = ttk.Button(root, text="Pair", command= lambda: pair(e1.get(), e2.get()))
b1.pack()


root.mainloop()
