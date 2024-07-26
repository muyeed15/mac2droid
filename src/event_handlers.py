from tkinter import Menu, messagebox
from tkinter.filedialog import askdirectory, askopenfile
import os

def openNewDirectory(dir_name, createDirectoryView, parent, current_target, directory_history):
    from src.gui import createDirectoryView

    directory_history.append(current_target[0])
    
    if current_target[0]:
        current_target[0] = f"{current_target[0]}/{dir_name}"
    else:
        current_target[0] = dir_name

    createDirectoryView(parent, current_target[0])

def goBack(createDirectoryView, parent, current_target, directory_history):
    from src.gui import createDirectoryView

    if directory_history:
        current_target[0] = directory_history.pop()
        createDirectoryView(parent, current_target[0])

def copyItem(item_path, current_target, parent):
    from src.gui import createDirectoryView
    directory = askdirectory()

    if directory:
        source_path = f"/storage/self/{current_target[0]}/{item_path}"
        os.system(f'adb pull "{source_path}" "{directory}"')
        createDirectoryView(parent, current_target[0])
        messagebox.showinfo("Copy", f"Copied item: {item_path} to {directory}")

def pasteItem(item_path, current_target, parent):
    from src.gui import createDirectoryView
    file = askopenfile()
    
    if file:
        file_path = file.name
        destination_path = f"/storage/self/{current_target[0]}/{item_path}"
        os.system(f'adb push "{file_path}" "{destination_path}"')
        createDirectoryView(parent, current_target[0])
        messagebox.showinfo("Paste", f"Pasted item: {item_path} from {file_path} to {destination_path}")

def pasteFolder(item_path, current_target, parent):
    from src.gui import createDirectoryView
    directory = askdirectory()

    if directory:
        destination_path = f"/storage/self/{current_target[0]}/{item_path}"
        os.system(f'adb push "{directory}/{item_path}" "{destination_path}"')
        createDirectoryView(parent, current_target[0])
        messagebox.showinfo("Paste", f"Pasted item: {item_path} from {directory} to {destination_path}")


def deleteItem(item_path, current_target, parent):
    from src.gui import createDirectoryView

    source_path = f"/storage/self/{current_target[0]}/{item_path}"
    os.system(f'adb shell rm -rf "{source_path}"')
    createDirectoryView(parent, current_target[0])
    messagebox.showinfo("Copy", f"Deleted item: {item_path}")


def showContextMenu(event, item_path, root, current_target):
    context_menu = Menu(root, tearoff=0)
    context_menu.add_command(label="Copy To", command=lambda: copyItem(item_path, current_target, root))
    context_menu.add_command(label="Copy From [file]", command=lambda: pasteItem(item_path, current_target, root))
    context_menu.add_command(label="Copy From [folder]", command=lambda: pasteFolder(item_path, current_target, root))

    if item_path != "":
        context_menu.add_command(label="Delete", command=lambda: deleteItem(item_path, current_target, root))

    context_menu.post(event.x_root, event.y_root)

def on_mouse_scroll(event, canvas, direction):
    canvas.yview_scroll(direction, "units")