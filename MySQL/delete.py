import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='college'
)

my_curs = mydb.cursor()

query = "DELETE FROM student WHERE name like %s"
val = ('Jay', )

my_curs.execute(query, val)

mydb.commit()

print("No. of rows deleted:", my_curs.rowcount)
