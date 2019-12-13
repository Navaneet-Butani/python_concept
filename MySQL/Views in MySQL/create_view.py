import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="college"
)

my_curs = mydb.cursor()

my_curs.execute("CREATE VIEW student_view AS SELECT id, name FROM student WHERE id>2")

print(type(my_curs))
