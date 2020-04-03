import os
import sqlite3

from Modules.files import get_db_path as db_path
from Modules.items import Item

def db_connect():
    """
    Create a sqlite3 database connection.
    Return database connection
    """

    connection = sqlite3.connect(db_path())
    return connection


def create_item_table():
    """
    Create table if database don't exist
    """

    # Get connection and cursor
    conn = db_connect()
    cursor = conn.cursor()

    # create table
    cursor.execute("""CREATE TABLE MARKET_ITEMS (
        NAME text,
        AVG_PRICE real,
        MIN_PRICE real,
        MAX_PRICE real,
        TIMES_ADDED integer
        )""")

    # commit and close
    conn.commit()
    conn.close()


def insert_one(item):
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO MARKET_ITEMS VALUES (?,?,?,?,?)", (
        item.name,
        item.avg_price,
        item.min_price,
        item.max_price,
        item.times_added
    ) )

    conn.commit()
    conn.close()


def insert_many(item_list):
    conn = db_connect()
    cursor = conn.cursor()

    for item in item_list:
        cursor.execute("INSERT INTO MARKET_ITEMS VALUES (?,?,?,?,?)", (
        item.name,
        item.avg_price,
        item.min_price,
        item.max_price,
        item.times_added
    ) )

    conn.commit()
    conn.close()


def select_all():
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM MARKET_ITEMS")
    items = cursor.fetchall()
    
    conn.commit()
    conn.close()

    return items


def get_names():
    item_list = select_all()
    names = []
    for item in item_list:
        names.append(item[0])
    return names


def update_one(item):
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute("""UPDATE MARKET_ITEMS SET 
    AVG_PRICE = :avg,
    MIN_PRICE = :min,
    MAX_PRICE = :max,
    TIMES_ADDED = :add

    WHERE NAME = :name""", 
    {   'avg':item.avg_price,
        'min':item.min_price,
        'max':item.max_price,
        'add':item.times_added,
        'name':item.name
    })
    
    conn.commit()
    conn.close()


def update_many(item_list):
    conn = db_connect()
    cursor = conn.cursor()

    for item in item_list:
        cursor.execute("""UPDATE MARKET_ITEMS SET 
        AVG_PRICE = :avg,
        MIN_PRICE = :min,
        MAX_PRICE = :max,
        TIMES_ADDED = :add

        WHERE NAME = :name""", 
        {   'avg':item.avg_price,
            'min':item.min_price,
            'max':item.max_price,
            'add':item.times_added,
            'name':item.name
        })
    
    conn.commit()
    conn.close()


def delete_one(item):
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute("DELETE from MARKET_ITEMS WHERE NAME = :name", {'name':item.name})
    
    conn.commit()
    conn.close()


def delete_many(item_list):
    conn = db_connect()
    cursor = conn.cursor()

    for item in item_list:
        cursor.execute("DELETE from MARKET_ITEMS WHERE NAME = :name", {'name':item.name})
    
    conn.commit()
    conn.close()


def get_item_dict():
    result = {}
    db_list = select_all()
    for obj in db_list:
        item = Item(obj[0],obj[1],obj[2],obj[3],obj[4])
        print(item)
        result[item.name] = item
    return result