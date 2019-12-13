import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="college"
)

my_curs = mydb.cursor()

query = "UPDATE student SET name='Jayesh' WHERE name='Jatin'"

my_curs.execute(query)

mydb.commit()

print("Affected rows:", my_curs.rowcount)
