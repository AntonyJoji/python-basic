import mysql.connector as my

def connect_to_database():
    con = my.connect(
        host="localhost",
        user="root",
        password="",
        database="sql123" 
        )
    return con
def create_table():
    con = connect_to_database()
    cursor = con.cursor()
    cursor.execute("CREATE TABLE python_table (id INT  PRIMARY KEY, name VARCHAR(255), location VARCHAR(255))")
    con.commit()
    con.close()
    

create_table()
