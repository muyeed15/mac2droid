from tkinter import Canvas, PhotoImage, Label, ttk
from src.adb_utils import fileList

current_target = [""]
directory_history = []

file_icons = {
    '.txt': 'txt.png',
    '.jpg': 'jpg.png',
    '.jpeg': 'jpg.png',
    '.png': 'png.png',
    '.gif': 'gif.png',
    '.bmp': 'bmp.png',
    '.txt': 'txt.png',
    '.webp': 'png.png',
    '.pdf': 'pdf.png',
    '.doc': 'docx.png',
    '.docx': 'docx.png',
    '.xls': 'xlsx.png',
    '.xlsx': 'xlsx.png',
    '.ppt': 'pptx.png',
    '.pptx': 'pptx.png',
    '.zip': 'zip.png',
    '.rar': 'zip.png',
    '.7z': 'zip.png',
    '.tar': 'zip.png',
    '.gz': 'zip.png',
    '.py': 'py.png',
    '.java': 'java.png',
    '.cpp': 'shell.png',
    '.c': 'shell.png',
    '.html': 'txt.png',
    '.css': 'shell.png',
    '.js': 'shell.png',
    '.mp4': 'vid.png',
    '.avi': 'vid.png',
    '.mov': 'vid.png',
    '.mkv': 'vid.png',
    '.wmv': 'vid.png',
    '.flv': 'vid.png',
    '.mp3': 'mus.png',
    '.wav': 'mus.png',
    '.aac': 'mus.png',
    '.ogg': 'mus.png',
    '.flac': 'mus.png',
    '.iso': 'zip.png',
    '.dmg': 'app.png',
    '.torrent': 'shell.png',
    '.apk': 'apk.png',
    '.psd': 'shell.png',
    '.ai': 'shell.png',
    '.svg': 'shell.png',
    '.raw': 'shell.png',
    '.epub': 'shell.png',
    '.mobi': 'shell.png',
    '.chm': 'shell.png',
    '.log': 'txt.png',
    '.sqlite': 'shell.png',
    '.db': 'shell.png',
    '.sql': 'shell.png',
    '.bat': 'shell.png',
    '.sh': 'shell.png',
    '.pl': 'shell.png',
    '.r': 'shell.png',
    '.md': 'txt.png',
    '.csv': 'shell.png',
    '.json': 'shell.png',
    '.yaml': 'shell.png',
    '.xml': 'shell.png',
    'default': 'folder.png'
}

def createDirectoryView(parent, target):
    from src.event_handlers import goBack, openNewDirectory, showContextMenu, on_mouse_scroll

    def truncate_text(text, max_length):
        if '.' in text:
            name, ext = text.rsplit('.', 1)
            ext = '.' + ext
        else:
            name, ext = text, ''
        
        truncated_name = name if len(name) <= (max_length - len(ext)) else name[:(max_length - len(ext)) - 3] + "..."
        
        return truncated_name + ext

    for widget in parent.winfo_children():
        widget.destroy()

    top_frame = ttk.Frame(parent)
    top_frame.pack(side="top", fill="x", padx=10, pady=10)

    path_button_frame = ttk.Frame(top_frame)
    path_button_frame.pack(side="top", fill="x", padx=10, pady=5)

    back_icon = PhotoImage(file="src/icon/back.png")
    refresh_icon = PhotoImage(file="src/icon/refresh.png")

    back_label = Label(path_button_frame, image=back_icon)
    back_label.image = back_icon
    back_label.pack(side="left")
    back_label.bind("<Button-1>", lambda event: goBack(createDirectoryView, parent, current_target, directory_history))

    refresh_label = Label(path_button_frame, image=refresh_icon)
    refresh_label.image = refresh_icon
    refresh_label.pack(side="right", padx=13)
    refresh_label.bind("<Button-1>", lambda event: createDirectoryView(parent, current_target[0]))

    path_parts = target.strip('/').split('/') if target else []
    current_path = ''

    def create_path_button(text, path):
        button = ttk.Button(path_button_frame, text=text, style="Path.TButton")
        button.pack(side="left", padx=5)
        return button

    create_path_button('/', '')
    for part in path_parts:
        current_path += f'/{part}'
        create_path_button(part, current_path)

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
    max_columns = 9

    max_name_length = 15

    for item in fileList(target):
        frame = ttk.Frame(button_frame)
        frame.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

        file_extension = item.rsplit('.', 1)[-1] if '.' in item else 'default'
        icon_file = file_icons.get(f'.{file_extension}', file_icons['default'])
        file_icon = PhotoImage(file="src/icon/"+icon_file)

        truncated_name = truncate_text(item, max_name_length)

        icon_label = Label(frame, image=file_icon, text=truncated_name, compound="top", font="Helvetica 12", wraplength=80, bd=0, highlightthickness=0)
        icon_label.image = file_icon
        icon_label.pack(side="top", padx=10, pady=(5, 0))

        icon_label.bind("<Button-1>", lambda event, item=item: openNewDirectory(item, createDirectoryView, parent, current_target, directory_history))
        icon_label.bind("<Button-2>", lambda event, item=item: showContextMenu(event, item, parent, current_target))
        icon_label.bind("<Button-3>", lambda event, item=item: showContextMenu(event, item, parent, current_target))

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