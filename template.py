import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

file_list = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "aap.py",
    "research/trials.ipynb"
]

for file_path in file_list:
    path = Path(file_path)
    folder, file = path.parent, path.name

    if folder != Path(""):
        os.makedirs(folder, exist_ok=True)
        logging.info(f"Creating directory: {folder} for the file: {file}")

    if (not path.exists()) or (path.stat().st_size == 0):
        with open(path, "w") as f:
            pass
        logging.info(f"Creating empty file: {path}")

    else:
        logging.info(f"{file} already exists")

