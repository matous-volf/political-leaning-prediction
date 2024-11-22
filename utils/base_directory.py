from pathlib import Path

# This is necessary when accessing file paths from e.g. Jupyter notebooks to use the correct context
# and not the directory of the notebook.
BASE_DIRECTORY = Path(__file__).resolve().parent.parent
