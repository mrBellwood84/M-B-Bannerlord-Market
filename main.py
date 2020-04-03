import os.path as path

from GUI.window import App
from Modules import database
from Modules.files import get_db_path
from Modules.items import Item

# Dict for importing items if database exist
items = {}

# Check if database exist
db_path = get_db_path()
db_exist = path.exists(db_path)

# create database if not exisst
if not db_exist:
    database.create_item_table()

# else, extract items from database and create list with item objects
else:
    items = database.get_item_dict()

# run app
runApp = App(items)
