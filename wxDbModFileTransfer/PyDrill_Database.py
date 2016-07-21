import sqlite3
import time
import datetime

conn = sqlite3.connect('fileTransfer.db')

def createTable():
    conn.execute("CREATE TABLE if not exists File_Transfer(\
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        date_time TEXT);")
    
def addEntry(date_time):
    val_str = "'{}'".format(date_time)
    sql_str = ("INSERT INTO File_Transfer(date_time) VALUES({});".format(val_str))
    conn.execute(sql_str)
    conn.commit()

def viewLast():
    sql_str = ("SELECT date_time FROM File_Transfer WHERE id = (SELECT(max(id)-1) FROM File_Transfer);")
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    return rows

def viewAll():
    sql_str = ("SELECT * FROM File_Transfer;")
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    print (rows)

createTable()
