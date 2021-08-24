import sqlite3 as lite

# functionality goes here

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                sql = "CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)"
                cur.execute(sql)
        except Exception:
            print("Unable to connect to the DB.")     

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                sql = "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)"
                cur.execute(sql, data)
                return True
        except Exception:
            return False

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                sql = "SELECT * FROM course"
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            return False

    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False



# TODO: provide interface to users

def main():
    print("Oscar Coto Calderon - Costa Rica\n")
    print("*"*40)
    print("\n:: COURSE MANAGEMENT ::\n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("\n:: USER MANUAL ::\n")
    print("#"*40)

    print('\n1. Insert a new Course\n')
    print('2. Show all Courses\n')
    print('3. Delete a Course (Need Id of the Course)\n')
    print("#"*40)
    print("\n")

    choice = input("\n Enter a choice: ")

    if choice == "1":
        print("\n:: Create a Course ::\n")
        name = input("\n Enter Course name: ")
        description = input("\n Enter Course description: ")
        price = input("\n Enter Course price: ")
        private = input("\n Is this a private Course? (0 - Private / 1 - Public) ")

        if db.insert_data([name, description, price, private]):
            print("\n Course was inserted succesfully\n")
        else:
            print("\n Course could not be inserted succesfully\n")
    
    elif choice == "3":
        print("\n:: Course List ::\n")
        print("-"*40)

        for index, item in enumerate(db.fetch_data()):
            print("\n Serial No. : " + str(index + 1) + "\n")
            print("\n Course ID : " + str(item[0]) + "\n")
            print("\n Course Name : " + str(item[1]) + "\n")
            print("\n Course Description : " + str(item[2]) + "\n")
            print("\n Course Price : " + str(item[3]) + "\n")
            private = 'Yes' if item[4] else 'No'
            print("\n Private Course? " + private + "\n")
            print("_"*40)
            print("\n")

    elif choice == "3":
        print("\n:: Delete a Course ::\n")
        course_id = input("\n Enter Course ID: ")
        
        if db.delete_data(course_id):
            print("\n Course was deleted succesfully\n")
        else:
            print("\n Course could not be deleted succesfully\n")
    
    else:
        print("\n Not a valid option\n")

if __name__ == '__main__':
    main()