import sqlite3

def query(query_text):
    conn=sqlite3.connect("Northwind_large.sqlite")
    cur = conn.cursor()
    cur.execute(query_text)
    rows = cur.fetchall()
    return rows
    conn.close()

def get_all_facts():
    return query(""" SELECT * FROM Supplier """)
