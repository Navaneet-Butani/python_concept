import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="college"
)

my_curs = mydb.cursor()

my_curs.execute("DROP VIEW student_view")

print(type(my_curs))
