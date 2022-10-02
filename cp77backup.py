import shutil
from datetime import date
from pathlib import Path
import os
import zipfile


def backup():
    save_path = Path.home().joinpath('Saved Games', 'CD Projekt Red')
    source = os.path.join(save_path, "Cyberpunk 2077")
    if not os.path.exists(source):
        print("Cyberpunk saved games folder cannot be located. Exiting.")
        return

    today = date.today()
    dst_format = "Cyberpunk 2077" + today.strftime("__%d_%b_%Y")
    destination = os.path.join(save_path, dst_format)

    print(f"Source: {source}\nDestination: {destination}")

    target_dir = shutil.copytree(source, destination, dirs_exist_ok=True)
    print(f"Backup raw folder size: {get_dir_size(target_dir)}")
    print("Done.")


def get_dir_size(target) -> str:
    raw_size: int = sum(p.stat().st_size for p in Path(target).rglob('*'))
    raw_size /= 1024
    return f"{raw_size:.1f}M"


backup()


# Save folder format 'Cyberpunk 2077_12_Jun_2022' as below maybe

