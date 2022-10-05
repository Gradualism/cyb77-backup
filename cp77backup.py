import shutil
from datetime import date
from pathlib import Path
import os
from tkinter import *


def backup() -> None:
    save_path = Path.home().joinpath('Saved Games', 'CD Projekt Red')
    source = os.path.join(save_path, "Cyberpunk 2077")

    lbl_result["text"] = check_source(source)

    today = date.today()
    dst_format = "Cyberpunk 2077" + today.strftime("__%d_%b_%Y")
    destination = os.path.join(save_path, dst_format)
    source_size = get_dir_size(source)
    target = shutil.make_archive(destination, "zip", source)
    target_size = get_file_size(target)

    lbl_result["text"] = f"Save folder size: {source_size}, compressed backup size: {target_size}. Done!"


def check_source(source) -> str:
    if not os.path.exists(source):
        return "Cyberpunk saved games folder cannot be located. Exiting."
    return "Save folder found."


def get_dir_size(target_dir) -> str:
    raw_size: int = sum(p.stat().st_size for p in Path(target_dir).rglob('*'))
    raw_size /= 1024
    return f"{raw_size:.1f}M"


def get_file_size(target_file) -> str:
    raw_size: int = os.path.getsize(target_file)
    raw_size /= 1024
    return f"{raw_size:.1f}M"


window = Tk()
window.title("Cyberpunk 2077 Savegame Backup")
window.columnconfigure(1, minsize=450)
window.rowconfigure(5, minsize=150)

btn_exec = Button(text="Backup", command=backup)

lbl_result = Label(text="Ready!")
lbl_intro = Label(text="Backup process does not alter your current save directory.")
lbl_note = Label(text="Backup your saves, choom. It'll save your ass one day.")

lbl_note.grid(row=3, column=0)
lbl_intro.grid(row=1, column=1)
btn_exec.grid(row=3, column=1)
lbl_result.grid(row=4, column=1)

window.mainloop()
