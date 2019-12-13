import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="college"
)

my_curs = mydb.cursor()

my_curs.execute("SELECT * FROM student_view")

result = my_curs.fetchall()

for record in result:
    print(record)