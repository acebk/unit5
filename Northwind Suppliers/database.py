import sqlite3

def query(query_text):
    conn=sqlite3.connect("Northwind_large.sqlite")
    cur = conn.cursor()
    cur.execute(query_text)
    #title = cur.description()
    rows = cur.fetchall()
    column_names = []
    #comp_name = []
    #city = []
    #country = []
    for col in cur.description:
        column_names.append(col[0])
    dicts = []
    #for row in rows:
        #column_names.append(row[0])
    for row in rows:
        r = [row[1], row[5], row[8]]
        d = dict(zip(column_names, r))
        dicts.append(d)
        #comp_name.append(row[1])
        #city.append(row[5])
        #country.append(row[8])
    conn.close()
    return dicts

def get_all_facts():
    return query(""" SELECT * FROM Supplier """)
