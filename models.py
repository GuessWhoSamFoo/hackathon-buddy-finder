import sqlite3 as sql

def create_new_idea(creator_name, creator_role, project_name, project_desc, spots, tags, position_one, position_one_owner, position_two, position_two_owner):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO ideas (creator_name, creator_role, project_name, project_desc, spots, tags, position_one, position_one_owner, position_two, position_two_owner) VALUES (?,?,?,?,?,?,?,?,?,?)", (creator_name, creator_role, project_name, project_desc, spots, tags, position_one, position_one_owner, position_two, position_two_owner))
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

def show_an_idea(id): 
    con = sql.connect("database.db")
    con.text_factory = str
    cur = con.cursor()
    cur.execute("SELECT * FROM ideas WHERE id = {id}".format(id=str(id)))
    one_idea = cur.fetchall()
    con.close()
    return one_idea