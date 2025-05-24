import os
from pathlib import Path


list_of_files=[

    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/helper.py",
    "init_setup.sh",
    "requirements.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "logger.py",
    "experiment/experiments.ipynb",
    "Dockerfile",
    ".gitignore",
    ".env",
    "app.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file