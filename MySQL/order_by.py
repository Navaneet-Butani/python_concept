import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='college'
)

my_curs = mydb.cursor()

# Select records in order of Names
query = "SELECT * FROM student ORDER BY name"

my_curs.execute(query)

result = my_curs.fetchall()

for record in result:
    print(record)


# Select data in DESCENDING ORDER
query_des = "SELECT * FROM student ORDER BY name DESC"

my_curs.execute(query_des)

result_des = my_curs.fetchall()

print("Data in descending order:")
for record in result_des:
    print(record)
