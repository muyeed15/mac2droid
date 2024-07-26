from tkinter import Tk
from src.gui import createDirectoryView
from src.helpers import root_geometry
from src.styles import apply_styles

def main():
    root = Tk()
    root.title("mac2droid : v0.0.1a")

    apply_styles()
    root_geometry(root, 1040, 600)

    createDirectoryView(root, "")

    root.mainloop()