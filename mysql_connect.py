import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Brodzik155",
    database="testdb"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Patryk")
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# mycursor.execute("SHOW TABLES")

# sql_formula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# students = [("Bob", 12),
#             ("Amanda", 32),
#             ("Jacob", 21),
#             ("Avi", 28),
#             ("Michelle", 17)]
# mycursor.executemany(sql_formula, students)
# mydb.commit()
# mycursor.execute("SELECT age FROM students")
# my_result = mycursor.fetchall()
# my_result = mycursor.fetchone()
# for row in my_result:
#     print(row)

