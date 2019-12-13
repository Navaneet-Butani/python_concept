import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='college'
)

my_curs = mydb.cursor()

# Select the data from the table 
my_curs.execute("SELECT * FROM student")

result = my_curs.fetchone() # Will fatch one recored only
print(result)

result_all = my_curs.fetchall() # Will fetch all the records


for record in result_all:
    print(record)


# Here we select the name and branch that grouped by branch and will just show only unique branches
my_curs.execute("SELECT name, branch FROM student GROUP BY branch ORDER BY id")

result_all = my_curs.fetchall() # Will fetch all the records

print("GROUP BY and ORDER BY result:")
for record in result_all:
    print(record)


# Here we use HAVING keyword
my_curs.execute("SELECT * FROM student HAVING id>3")
result_all = my_curs.fetchall() # Will fetch all the records

print("HAVING result:")
for record in result_all:
    print(record)


my_curs.execute()
