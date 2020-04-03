import os

# Get root directory
def get_root():
    return os.path.dirname(os.path.abspath("main.py"))

# Get database directory
def get_db_path():
    root = get_root()
    return os.path.join(root, "Data\\data.db")