import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='college'
)

my_curs = mydb.cursor()

# Drop specific column
my_curs.execute("ALTER TABLE student DROP city")

# # Remove the table if that table is existed into the database
my_curs.execute("DROP TABLE IF EXISTS student")
