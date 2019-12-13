import mysql.connector

# Create Database
mydb = mysql.connector.connect(
  host="localhost",   
  user="root",   # Specifies the user name of the system
  passwd="123"  # Password for that specified user
)

print("Databases:", mydb)

# Specify the cursor to work with
my_curs = mydb.cursor()

# Create Database
my_curs.execute("CREATE DATABASE college")

my_curs.execute("SHOW DATABASES")

# Print all the existd databases
for db in my_curs:
  print("Database:", db)
