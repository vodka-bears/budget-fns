# Basically, fuck it

from receipt import Receipt, Entry
import sqlite3

def new_db(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE receipts (
            id PRIMARY KEY
            rawdata text,
            paid_sum real,
            sum real,
            nds10 real,
            nds18 real,
            strtime text,
            operator text,
            user text,
            inn text,
            optype integer,
            fn text,
            fd text,
            fpd text
        """
    )
    cur.execute(
        """
        CREATE TABLE entries (
            name text,
            barcode text,
            price real,
            
            
        """
    )

def add_receipt(r, dbname):
    