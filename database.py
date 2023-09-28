import sqlite3
from sqlite3 import Error


# begin sql connection
def sql_connection():
    try:
        conDatabase = sqlite3.connect('data_app.db')
        conDatabase.execute("PRAGMA foreign_keys = ON")
        return conDatabase

    except:
        print(Error)


conDatabase = sql_connection()
