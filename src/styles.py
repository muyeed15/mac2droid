from tkinter import ttk

def apply_styles():
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12))
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TFrame', background='#f0f0f0')
    style.configure('TScrollbar', troughcolor='#d4d4d4', bordercolor='#d4d4d4', background='#e0e0e0')