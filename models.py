import sqlite3 as sql

def create_new_idea(author, title, description, max_num):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO ideas (author, title, description, max_num) VALUES (?,?,?,?)", (author, title, description, max_num))
    con.commit()
    con.close()
    
def show_all_ideas():
    con = sql.connect("database.db")
    con.text_factory = str
    cur = con.cursor()
    cur.execute("SELECT * FROM ideas")
    entries = cur.fetchall()
    con.close()
    return entries