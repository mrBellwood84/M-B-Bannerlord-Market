# Bannerlord Market

While gaming Mount&Blade Bannerlord, I thougt it wold be fun to make small program that kept track of the average price of items in city markets. It would make it a bit easier to keep track of prices and profit margins during the game.

Trading is not the best way to make money in the game, it sure was a great weekend project for coding.

The GUI is created with TKinter, and data is stored in a sqlite database.

## How it works:

The program is not compiled and have to be run as a python script
```bash
py main.py
```

When first opened, the program will create a new sqlite database.

User can add new items to the menu.

When an item is added, the user can add a price to the item. User can also undo the last edited price to the item. Items can also be removed.

The field for each items contain the info __[average price | lowest price  | highest price]__.

User must click save to save data to the database. Loading will load data from the database, overwriting any unsaved data.