from tkinter import Canvas, Button, ttk
from src.adb_utils import fileList

current_target = [""]
directory_history = []

def createDirectoryView(parent, target):
    from src.event_handlers import goBack, openNewDirectory, showContextMenu, on_mouse_scroll

    for widget in parent.winfo_children():
        widget.destroy()

    top_frame = ttk.Frame(parent)
    top_frame.pack(side="top", fill="x", padx=10, pady=10)

    path_button_frame = ttk.Frame(top_frame)
    path_button_frame.pack(side="top", fill="x", padx=10, pady=5)

    back_button = ttk.Button(path_button_frame, text="Back", command=lambda: goBack(createDirectoryView, parent, current_target, directory_history))
    back_button.pack(side="left")

    path_label = ttk.Label(path_button_frame, text=f"/{target if target else '/'}")
    path_label.pack(side="left", padx=5, expand=True)

    refresh_button = ttk.Button(path_button_frame, text="Refresh", command=lambda: createDirectoryView(parent, current_target[0]))
    refresh_button.pack(side="right", padx=13)

    canvas = Canvas(parent)
    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)

    button_frame = ttk.Frame(canvas)

    canvas.create_window((0, 0), window=button_frame, anchor="nw")

    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    canvas.bind("<Button-2>", lambda event: showContextMenu(event, "", parent, current_target))
    canvas.bind("<Button-3>", lambda event: showContextMenu(event, "", parent, current_target))

    row, column = 0, 0
    max_columns = 4
    button_width = 32
    button_height = 5

    for item in fileList(target):
        button = Button(button_frame, text=item, width=button_width, height=button_height, font="Helvetica, 12", command=lambda item=item: openNewDirectory(item, createDirectoryView, parent, current_target, directory_history))
        button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")

        button.bind("<Button-2>", lambda event, item=item: showContextMenu(event, item, parent, current_target))
        button.bind("<Button-3>", lambda event, item=item: showContextMenu(event, item, parent, current_target))

        column += 1
        if column == max_columns:
            column = 0
            row += 1

    button_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    if canvas.bbox("all")[3] > canvas.winfo_height():
        canvas.bind_all("<Button-4>", lambda event, canvas=canvas: on_mouse_scroll(event, canvas, -1))
        canvas.bind_all("<Button-5>", lambda event, canvas=canvas: on_mouse_scroll(event, canvas, 1))
        parent.bind_all("<MouseWheel>", lambda event, canvas=canvas: on_mouse_scroll(event, canvas, -1 if event.delta > 0 else 1))
    else:
        canvas.unbind_all("<Button-4>")
        canvas.unbind_all("<Button-5>")
        parent.unbind_all("<MouseWheel>")