import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="college"
)

my_curs = mydb.cursor()

# Create the student table
my_curs.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), branch VARCHAR(25), city VARCHAR(25))")

# Delete column from the table
# my_curs.execute("ALTER TABLE student DROP city")