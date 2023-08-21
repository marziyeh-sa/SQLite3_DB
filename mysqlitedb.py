import sqlite3
from sqlite3 import Error


def sqlite_connector(name_db):

    con = sqlite3.connect(name_db)
    cur = con.cursor()
    return con, cur


def create_table(cur, con):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS STUDENTS(id integer PRIMARY KEY, name text, age integer, department text)"
    )
    con.commit()


def insert_data(cur, con):
    cur.execute(
        "INSERT INTO STUDENTS VALUES(1, 'Sama', 27, 'Data science')"
    )
    con.commit()


def insert_many(cur, con, entity):
    cur.executemany(
        "INSERT OR IGNORE INTO STUDENTS VALUES(?,?,?,?)",
        entity
    )
    con.commit()


con, cur = sqlite_connector('Mysqlitedb.db')
# create_table( cur, con)
# insert_data( cur, con)
data = [(1,"Saman", 29, "Data"), (2,"Ali", 12, "student")]
insert_many(cur, con, data)
