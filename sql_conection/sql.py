from unittest import result

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
    

# create_table()

# def insert_data(id, name, location):
#     con= connect_to_database()
#     cursor = con.cursor()
#     cursor.execute(f"INSERT INTO python_table VALUES ({id}, '{name}', '{location}')")
#     con.commit()
#     con.close()
#     cursor.close()

# insert_data(1, "John Doe", "New York")
# insert_data(2, "Jane Smith", "Los Angeles")

# def fetch_data():
#     con = connect_to_database()
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM python_table")
#     result = cursor.fetchall()
#     for row in result:
#         print(row)

#     con.close()
#     cursor.close()

# fetch_data()

# def drop_table(table_name):
#     con = connect_to_database()
#     cursor = con.cursor()
#     cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
#     con.commit()
#     con.close()
#     cursor.close()

# drop_table("python_table")

def add_column(table_name, column_name, data_type):
    con = connect_to_database()
    cursor = con.cursor()
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type}")
    con.commit()
    con.close()
    cursor.close()

# add_column("python_table", "age", "INT")
add_column("python_table", "email", "VARCHAR(255)")
