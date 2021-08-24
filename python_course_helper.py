import sqlite3 as lite

# functionality goes here

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)"
                    )
        except Exception:
            print("Unable to connect to the DB.")     

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data
                    )
                return True
        except Exception:
            return False

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM courses")
                return cur.fetchall()
        except Exception:
            return False

    def delete_data(self, id):
        pass



# TODO: provide interface to users