import shutil
from datetime import date
from pathlib import Path
import os
import sys


# OS Pathing
home_dir = Path.home()
filepath = Path.home().joinpath('Saved Games', 'CD Projekt Red', 'Cyberpunk 2077')

# Verify directory present
if not os.path.exists(filepath):
    print("Cyberpunk saved games folder cannot be located. Exiting.")

# Check destination doesn't already exist

# Copy folder with new name

# Save folder format 'Cyberpunk 2077_12_Jun_2022' as below maybe
today = date.today()
date_format = today.strftime("_%d_%b_%Y")

