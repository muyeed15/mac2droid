def root_geometry(root, root_width, root_height):
    root.geometry(f"{root_width}x{root_height}+"
                  f"{int((root.winfo_screenwidth() - root_width) / 2)}+"
                  f"{int((root.winfo_screenheight() - root_height) / 2) - 40}")
    root.resizable(False, False)