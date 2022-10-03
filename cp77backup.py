import shutil
from datetime import date
from pathlib import Path
import os


def backup():
    save_path = Path.home().joinpath('Saved Games', 'CD Projekt Red')
    source = os.path.join(save_path, "Cyberpunk 2077")
    if not os.path.exists(source):
        print("Cyberpunk saved games folder cannot be located. Exiting.")
        return

    today = date.today()
    dst_format = "Cyberpunk 2077" + today.strftime("__%d_%b_%Y")
    destination = os.path.join(save_path, dst_format)

    print(f"Source: {source}\nDestination: {destination}")  # Do we need to keep this?

    source_size = get_dir_size(source)

    print("Compressing backup, please wait ...")
    target = shutil.make_archive(destination, "zip", source)

    target_size = get_file_size(target)

    print(f"Save folder size: {source_size}, compressed backup size: {target_size}")
    print("Done.")


def get_dir_size(target_dir) -> str:
    raw_size: int = sum(p.stat().st_size for p in Path(target_dir).rglob('*'))
    raw_size /= 1024
    return f"{raw_size:.1f}M"


def get_file_size(target_file) -> str:
    raw_size: int = os.path.getsize(target_file)
    raw_size /= 1024
    return f"{raw_size:.1f}M"


backup()
