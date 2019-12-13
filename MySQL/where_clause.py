import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='college'
)

my_curs = mydb.cursor()

# Apply selection with WHERE Clouse
query = "SELECT * FROM student WHERE name = 'Jay'"

my_curs.execute(query)

where_result = my_curs.fetchall()

for record in where_result:
    print(record)


# Selecting with wildcard character
query = "SELECT * FROM student WHERE name LIKE '%t%'"   # This will give only those result which are matching the the 't'
my_curs.execute(query)

card_result = my_curs.fetchall()

for record in card_result:
    print(record)

