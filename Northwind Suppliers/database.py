import sqlite3

def query(query_text):
    conn=sqlite3.connect("Northwind_large.sqlite")
    cur = conn.cursor()
    cur = execute(query_text)

    
